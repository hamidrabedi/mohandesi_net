from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from decouple import config

from .views import Home, searchbox


urlpatterns = [
   path('admin/', admin.site.urls),
   path('search/',searchbox, name='serachbox'),
   path('' , Home.as_view() ,  name='home'),
   path('comment/',include('comment.urls', namespace='comment')),
   path('product/',include("product.urls",namespace="product") ),
   path("user/", include("user.urls", namespace='user')),
   path('oauth/', include('social_django.urls', namespace='social')),
]


if config("DEBUG_TOOLBAR", default=False):
   import debug_toolbar
   urlpatterns += static(
      settings.STATIC_URL,
      document_root=settings.STATIC_ROOT
   )
   urlpatterns += static(
      settings.MEDIA_URL,
      document_root=settings.MEDIA_ROOT
   )
   urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))
