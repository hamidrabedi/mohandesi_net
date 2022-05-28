from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from decouple import config


urlpatterns = [
   path('admin/', admin.site.urls),
   path('comment/',include('comment.urls', namespace='comment')),
   path('product/',include("product.urls",namespace="product") ),
   path("user/", include("user.urls", namespace='user')),
   path('', include('pages.urls')),
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
