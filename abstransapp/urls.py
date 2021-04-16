from django.urls import path
from .views import home, abstrans

urlpatterns = [
    path('', home, name='index'),
    path('abstrans/', abstrans, name='abstrans'),
]
