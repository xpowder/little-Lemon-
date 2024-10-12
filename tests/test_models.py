from django.test import TestCase
from restaurant.models import Booking, Menu

class MenuTest(TestCase):
    def test_get_items(self):
        menu = Menu.objects.create(name="Icecream", price=80.00, inventory=100)
        self.assertEqual(str(menu), "Icecream : 80.0")
