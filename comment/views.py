from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from comment.forms import CommentForm

from product.models import Product
from user.models import User


@login_required(login_url="/user/login/")
def add_comment(request, product_id):
    
    form = CommentForm(request.POST or None)
    if request.method == "POST":
        product = get_object_or_404(Product, id=product_id)
        customer=get_object_or_404(User,email=request.user.email)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = customer
            comment.product = product
            comment.save()
            return redirect("product:detailproduct",int(product_id))    
    else:
        return redirect("product:detailproduct",int(product_id))
