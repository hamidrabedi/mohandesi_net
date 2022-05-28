from product.models import Category


def header(request):
        parent=[]
        parent_cat=Category.objects.all().filter(parent=None).order_by('title')
        for cat in parent_cat:
            parent.append(cat.child.all())
        context = { 
        'parent_cats':parent_cat, 
        'sub_cats':parent,  
        }
        return context



