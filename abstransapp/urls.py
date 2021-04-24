from django.urls import path
from .views import home, abstrans, search

urlpatterns = [
    path('', home, name='index'),
    path('search/', search, name='search'),
    path('abstrans/<path:doi>', abstrans, name='abstrans'),
]
