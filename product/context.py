from product.models import Category


def header(request):
        sub_cats=[]
        parent_cat=Category.objects.all().filter(parent=None).order_by('title')
        for cat in parent_cat:
            sub_cats.append(cat.child.all())
        context = { 
        'parent_cats':parent_cat, 
        'sub_cats':sub_cats,  
        }
        return context



