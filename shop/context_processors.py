from .models import Category
from .views import allProdCat


def menu_links(request):
    links=Category.objects.all()
    return dict(links=links)