from django.test import TestCase
from restaurant.models import *


class MenuModelTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Ice Cream", price=80.33, inventory=15)
        self.assertEqual(item.title, "Ice Cream")
        self.assertEqual(item.price, 80.33)
        self.assertEqual(item.inventory, 15)
