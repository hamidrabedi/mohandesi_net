import random
import secrets

from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.core.management.base import (
    BaseCommand,
)

from faker import Faker
from tqdm import tqdm

from product.models import (
    Category,
    Product,
    Property,
    Details,
)

User = get_user_model()
fake = Faker(['fa-IR'])

class Command(BaseCommand):
    help = ('Generate data for product models')

    def handle(self, *args, **kwargs):
        user = self.make_user()

        # ========> CATEGORY
        self.create_bulk_categories()
        self.stdout.write(self.style.SUCCESS(
            f'5 Parent Categories were created successfully.'))
        self.stdout.write(self.style.SUCCESS(
            f'25 Categories were created successfully.'))

        # ========> ATTRIBUTE
        atts= self.create_bulk_categories_attributes()
        self.stdout.write(self.style.SUCCESS(
            f'{len(atts)} attributes were created successfully.'))

        # ========> DETAIL
        details= self.create_details()
        self.stdout.write(self.style.SUCCESS(
            f'{len(details)} details were created successfully.'))

        # ========> PRODUCT
        products= self.create_product()
        self.stdout.write(self.style.SUCCESS(
            f'{len(products)} products were created successfully.'))

    def make_user(self):
        user, created = User.objects.get_or_create(email='generator@gen.com')
        if created:
            user.set_password(secrets.token_urlsafe(16))
            user.is_active = False
            user.is_superuser = False
            user.save()
        return user

    def create_bulk_categories(self):
        print(f'!!! GENERATING 5 PARENT CATEGORIES !!!')
        parents_obj = [Category(
            title=f'cat-{index}',
            parent=None,
        )
            for index in range(5)
        ]

        parents = Category.objects.bulk_create(parents_obj)

        print(f'!!! GENERATING 25 CHILD CATEGORIES !!!')
        children_obj = [Category(
            title=f'child-{index}',
            parent=parents[index//5],
        )
            for index in range(5 * 5)
        ]

        children = Category.objects.bulk_create(children_obj)

    def create_bulk_categories_attributes(self):
        print(f'!!! GENERATING 1 PROPERTY FOR EACH CATEGORY !!!')
        cats = Category.objects.all()
        attributes = [Property(
            title=f'property-{index}',
            category=cats[index],
        )
            for index in tqdm(range(cats.count()))
        ]
        return Property.objects.bulk_create(attributes)

    def create_product(self):
        print(f'!!! GENERATING 200 PRODUCTS !!!')
        child_categories= Category.objects.filter(parent__isnull=False)

        products = [
            Product(
                title=f'Product-{i}',
                description=fake.paragraph(nb_sentences = 8),
                brand=f'brand-{i}',
                price=random.randint(1000,1000000),
                in_stock=random.randint(0,10),
                is_active=random.choice([True, False]),
                img='prod_image1.jpg',
                img1='prod_image2.jpg',
                img2='prod_image3.jpg',
                category=child_categories[i%child_categories.count()],
                slug=slugify(f'Product-{i}'),
            )
            for i in tqdm(range(200))
        ]
        products= Product.objects.bulk_create(products)

        print(f'!!! SETTING ATTRIBUTES FOR  PRODUCTS !!!')
        details= Details.objects.all()
        for product in tqdm(products):
            possible_details= list(details.filter(property__category=product.category))
            product.attributes.add(random.choice(possible_details))

        return products

    def create_details(self):
        print(f'!!! GENERATING 3 DETAIL FOR EACH PROPERTY !!!')
        
        # products= Product.objects.all().select_related('category').prefetch_related('category__properties')
        properties= Property.objects.all()
        details= []
        for i in tqdm(range(3 * properties.count())):
            details.append(
                Details(
                    property=properties[i//3],
                    detail=f'detail-{i}'
                )
            )

        return Details.objects.bulk_create(details)