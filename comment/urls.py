

from django.urls import path
from comment.views import add_comment


app_name='comment'


urlpatterns = [
    path('comment/<int:product_id>', add_comment ,name='comment'),
]
