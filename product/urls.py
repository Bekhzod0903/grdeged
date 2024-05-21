from django.urls import path
from .views import *

app_name = 'product'
urlpatterns = [
    path('test/', ListView.as_view(), name='food-list'),
]