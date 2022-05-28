

from django.contrib.auth import authenticate, logout as _logout, login as _login,get_user_model

from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods
from django.views.generic import DetailView

from user.forms import ForgetPassForm, ForgetPasswordForm, RegisterForm ,LoginForm


User = get_user_model()

@require_http_methods(["GET", "POST"])
def login(request):
    login_form = LoginForm(request.POST or None)
    if request.method == "GET":
        next = request.GET.get("next", "")
        
        if next:
            return render(request, 'User/login_page.html', {'login_form': login_form,'next':next})
        else:
            return render(request, 'User/login_page.html', {'login_form': login_form,})
            
    else:
        if login_form.is_valid():
            email = request.POST.get("email", "")
            password = request.POST.get("password", "")
            user = authenticate(request, email=email, password=password)
            if user is not None:  
                _login(request, user)
                next = request.GET.get("next", "")
                if next:
                    return redirect('home')
                return redirect('home')
            else:
                return render(request, 'User/login_page.html', {'login_form': login_form})
        else:
            return render(request, 'User/login_page.html', {'login_form': login_form})


def logout(request):
    _logout(request)
    return redirect('home')


def register(request):
    register_form = RegisterForm(request.POST or None)
    if request.method == "GET":
        return render(request, 'User/register_page.html', {'register_form': register_form})
    elif request.method == "POST":
        if register_form.is_valid():
            user=register_form.save(commit=False)
            user.is_active = False
            user.save()
            return redirect('user:login')
        else:
            return render(request, 'User/register_page.html', {'register_form': register_form})


def activate(request, valid, backend='django.contrib.auth.backends.ModelBackend'):
    user=Profile.objects.get(email=request.session.get("email"))
    ucode=cache.get(request.session.get("email"))
    if request.session.get("uid")==ucode:
        user.is_active=True
        user.save()
        _login(request,user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect("home")
    else:
        return redirect("user:register")

class show_user(DetailView):
    model=User
    template_name="User/profile.html"
    context_object_name="profile_item"
    pk_url_kwarg="id"