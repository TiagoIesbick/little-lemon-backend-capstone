from django.test import TestCase, RequestFactory
from restaurant.models import Menu
from restaurant.views import MenuItemsView
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.menu_0 = Menu.objects.create(
            title="Pasta",
            price=15.99,
            inventory=25
        )
        self.menu_1 = Menu.objects.create(
            title="Pizza",
            price=21.50,
            inventory=50
        )

    def test_getall(self):
        request = self.factory.get('/restaurant/menu')
        response = MenuItemsView.as_view()(request)
        self.assertEqual(response.data[0], MenuSerializer(self.menu_0).data)
        self.assertEqual(response.data[1], MenuSerializer(self.menu_1).data)
