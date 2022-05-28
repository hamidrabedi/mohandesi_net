import pytz
import random
from datetime import datetime

from django.core.management.base import (
    BaseCommand,
)

from faker import Faker
from tqdm import tqdm

from pages.models import (
    TopBanner,
    Advertisement,
    OtherProducts,
)
from product.models import Product

fake = Faker(['fa-IR'])

class Command(BaseCommand):
    help = ('Generate data for product models')

    def handle(self, *args, **kwargs):

        # ========> Top Banner
        self.create_top_banner()
        self.stdout.write(self.style.SUCCESS(
            f'Banners created successfully'))

        # ========> Advertisement
        ads= self.create_ads()
        self.stdout.write(self.style.SUCCESS(
            f'{len(ads)} Ads created successfully'))

        # ========> OTHER PRODUCTS
        ads= self.create_other_products()
        self.stdout.write(self.style.SUCCESS(
            f'50 products added to OTHER PRODUCTS successfully'))


    def create_top_banner(self):
        print(f'!!! GENERATING 5 BANNERS !!!')
        banners = [TopBanner(
            header=f'TOP HEADER {index}',
            green_text=f'GREEN TEXT {index}', 
            white_text=f'WHITE TEXT {index}',
            description=fake.paragraph(nb_sentences = 2),
            image='banner.png',
            url='https://google.com',
            is_active=True
        )
            for index in tqdm(range(5))
        ]

        TopBanner.objects.bulk_create(banners)

    def create_ads(self):
        print(f'!!! GENERATING ADVERTISEMENTS !!!')
        choices =[
            'tl',
            'tm',
            'tr',
            'br',
            'bl',
        ]
        ads= [Advertisement(
            title=f'ads title {i}',
            position= choices[i],
            img='prod_image1.jpg',
            alternate_text=f'alternate text {i}',
            url_redirect='https://google.com',
            publication_date_start= datetime(datetime.now().year-1,
                                        random.randint(1,12),
                                        random.randint(1,28),
                                        random.randint(0,23),
                                        random.randint(1,59),
                                        random.randint(1,59),
                                        random.randint(1,100),
                                        tzinfo=pytz.UTC
            ),
            publication_date_end= datetime(datetime.now().year+2,
                                        random.randint(1,12),
                                        random.randint(1,28),
                                        random.randint(0,23),
                                        random.randint(1,59),
                                        random.randint(1,59),
                                        random.randint(1,100),
                                        tzinfo=pytz.UTC
            )
        )
        for i in tqdm(range(5))
    ]
        return Advertisement.objects.bulk_create(ads)

    def create_other_products(self):
        print(f'!!! GENERATING OTHER PRODUCTS !!!')
        products = Product.objects.all()
        other_prod= OtherProducts.objects.create()
        other_prod.products.add(*products[100:150])