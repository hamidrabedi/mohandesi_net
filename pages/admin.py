from django.contrib import admin

from .models import(
    TopBanner,
    Advertisement,
    OtherProducts
)


admin.site.register(TopBanner)
admin.site.register(Advertisement)
admin.site.register(OtherProducts)