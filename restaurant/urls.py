from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('', index, name='home'),
    path('menu', MenuItemsView.as_view(), name='menu'),
    path('menu/<int:pk>', SingleMenuItemView.as_view(), name='menu_item'),
    path('api-token-auth', obtain_auth_token),
]
