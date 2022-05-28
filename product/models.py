from django.utils.translation import gettext as _
from user.models import User
from django.db import models
from django.utils.text import slugify
from django.shortcuts import get_object_or_404

class Category(models.Model):
    title=models.CharField(
        max_length=150
        )
    parent=models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='child'
        )

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    @classmethod
    def get_cat(cls,id):
        cat = get_object_or_404 (Category,pk = id)
        return cat

    def __str__(self) -> str:
        return self.title


class Product(models.Model):
    title=models.CharField(max_length=150)
    description=models.TextField(null=True)
    brand=models.CharField(max_length=50,null=True ,blank=True)
    price=models.BigIntegerField(null=True)
    in_stock=models.PositiveIntegerField(null=True)
    is_active=models.BooleanField(default=False)
    img=models.ImageField(upload_to="products/",null=True,blank=True)
    img1=models.ImageField(upload_to="products/",null=True,blank=True)
    img2=models.ImageField(upload_to="products/",null=True,blank=True)
    date_create=models.DateField(auto_now_add=True)
    date_update=models.DateField(auto_now=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE,  related_name='products' )
    slug = models.SlugField(null=True, unique=True, blank=True)
    attributes = models.ManyToManyField(
        'Details',
        related_name='products'
    )

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    @property
    def return_category(self):
        cat=Category.objects.get(pk=self.category.id)
        return cat

    @property
    def comments(self):
        return self.comments.all()

    @property
    def get_possible_attributes(self):
        return self.category.properties.details.all()
    
    def __str__(self) -> str:
        return self.title


    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        return super().save(*args, **kwargs)


class Property(models.Model):
    title=models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    category=models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='properties'
    )

    @property
    def details(self):
        return self.details.all()

    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"

    def __str__(self) -> str:
        return self.title


class Details(models.Model):
    property=models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name='details'
    )
    detail=models.CharField(
        max_length=400,
        null=True,
        blank=True
    ) 
    class Meta:
        verbose_name = "Detail"
        verbose_name_plural = "Details"

    def __str__(self) -> str:
        return self.detail


class WishList(models.Model):
    user=models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="wishlist"
    )
    product=models.ManyToManyField(Product)
    datetime =models.DateTimeField(
        auto_now=True,
        verbose_name=_('date and time')
    )

    class Meta:
        verbose_name = "Wishlist"
        verbose_name_plural = "Wishlists"

    def __str__(self):
        return self.user.email


