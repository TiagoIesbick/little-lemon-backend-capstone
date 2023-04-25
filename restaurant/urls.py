from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('menu', MenuItemsView.as_view(), name='menu'),
    path('menu/<int:pk>', SingleMenuItemView.as_view(), name='menu_item'),
]