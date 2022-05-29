from django.urls import path

from pages.views import Home, RaiseException

urlpatterns= [
    path('' , Home.as_view() ,  name='home'),
    path('exception/' , RaiseException.as_view() ,  name='raise_exception'),
    
]