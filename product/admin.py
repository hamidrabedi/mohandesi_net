from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe

from product.models import Category, Details, Product, Property, WishList


admin.site.register(WishList) 

class DetailItemInline(admin.StackedInline):
    model = Details

@admin.register(Property)
class PropertyModelAdmin(admin.ModelAdmin):
    list_display=[
        'title',
        'category'
    ]
    list_select_related =['category']
    list_filter = ['category']
    inlines = [DetailItemInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=[
        'title',
        'is_parent'
    ]
    empty_value_display = '-NA-'
    list_filter = ['parent']

    @admin.display(description='parent')
    def is_parent(self, obj):
        parameters = ('#f46a6a', 'MAIN',) if obj.child.all() else (
            'fff', obj.parent,)
        data_point = '<span style="color: {};">{}</span>'.format(*parameters)
        return mark_safe(data_point)

    def get_queryset(self, request):
        qs = Category.objects.all().select_related('parent').prefetch_related('child')
        return qs

@admin.register(Details)
class DetailAdmin(admin.ModelAdmin):
    list_display= [
    'property',
    'detail'
    ]


class ProductAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['attributes'].queryset = Details.objects.filter(property__in=self.instance.category.properties.all())
    class Meta:
        model = Product
        fields = '__all__'
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form= ProductAdminForm
    list_display=[
        'title',
        'brand',
        'price',
        'in_stock',
        'is_active',
        'date_create',
        'date_update',
        'category',
    ]
    empty_value_display = '-NA-'
    list_filter=['date_create']
    list_editable = ['in_stock']
    raw_id_fields = ['category']
    filter_horizontal = ['attributes']
