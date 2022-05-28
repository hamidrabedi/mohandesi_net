from django.db import models
from user.models import User
from product.models import Product
from django.utils.translation import gettext as _



class rate(models.Model):
    RATE_CHOICES=[
        ("1","1"),
        ("2","2"),
        ("3","3"),
        ("4","4"),
        ("5","5")
    ] 

    user=models.ForeignKey(
        User
        ,on_delete=models.CASCADE,
        related_name="rates",
        verbose_name=_("user")
    )
    product=models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="rates",
        verbose_name=_("product")
    )
    rate=models.CharField(
        max_length=1,
        choices=RATE_CHOICES,verbose_name=_("rate"),
        help_text="امتیاز خود را وارد کنید",
        null=True,
        blank=True
    )

    class Meta:
        verbose_name="rate"
        verbose_name_plural="rates"

    def __str__(self) -> str:
        return self.user.first_name

class CommentMe(models.Model):
    user=models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        related_name="comments",
        verbose_name=_("comment")
    )   
    product=models.ForeignKey(
        Product,on_delete=models.CASCADE,
        related_name="comments",
        verbose_name=_("product")
    )
    comment=models.CharField(
        max_length=255,
        verbose_name=_("comment"),
        help_text="کامنت خود را وارد کنید",
        null=True,
        blank=True
    )

    class Meta:
        verbose_name="comment"
        verbose_name_plural="comments"

    def __str__(self) -> str:
        return self.id