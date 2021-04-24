from django.urls import path
from .views import home, abstrans, search
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', home, name='index'),
    path('search/', search, name='search'),
    path('abstrans/<path:doi>', cache_page(60 * 15)(abstrans), name='abstrans'),
]
