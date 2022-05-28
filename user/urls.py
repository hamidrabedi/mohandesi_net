from django.urls import path

from .views import *


app_name="user"

urlpatterns = [
#----------------restless url----------------------
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("register/", register, name="register"),
    path('user/<int:id>',show_user.as_view(),name="user"),

]