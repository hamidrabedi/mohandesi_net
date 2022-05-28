from django.db import models
from django.core.exceptions import ValidationError


class TopBanner(models.Model):
    header = models.CharField(
        'Header text',
        max_length=100
        )
    green_text = models.CharField(
        'Green text',
        max_length=250
    )
    white_text = models.CharField(
        'White text',
        max_length=250
    )
    description = models.CharField(
        'Description',
        max_length=450
    )
    image = models.ImageField(
        upload_to="products/",
        null=True,
        blank=True
    )
    url = models.URLField(
        'URL',
    )
    is_active = models.BooleanField(
        'is active',
        default=False
    )

    def __str__(self):
        return self.header

    def __repr__(self):
        return self.header

class Advertisement(models.Model):
    CHOICES =(
        ('tl', 'Top Left'),
        ('tm', 'Top Mid'),
        ('tr', 'Top Right'),
        ('br', 'Bottom Right'),
        ('bl', 'Bottom Left'),
    )
    title=models.CharField(
        'Title',
        max_length=150
    )
    position=models.CharField(
        'Position',
        choices=CHOICES,
        max_length=2
    )
    img=models.ImageField(
        'Image',
        upload_to="ads/"
    )
    alternate_text= models.CharField(
        'Alternate Text',
        max_length=255,
        blank=True
    )
    url_redirect = models.URLField(
        ('Website URL'),
        help_text = ("URL of the website that this Ad leads to ")
    )
    publication_date_start = models.DateTimeField(
        ("Start of this Ad")
    )
    publication_date_end = models.DateTimeField(
        ("End of this Ad")
    )

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

class OtherProducts(models.Model):
    products= models.ManyToManyField(
        'product.Product'
    )

    def clean(self, *args, **kwargs):
        if self._state.adding:
            if OtherProducts.objects.all().count() > 1:
                raise ValidationError('You can not have more than one of this model')

    class Meta:
        verbose_name = "Other Product"
        verbose_name_plural = "Other Products"