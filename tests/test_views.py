from django.test import TestCase
from restaurant.views import index, MenuItemsView, SingleMenuItemView, BookingViewSet
from restaurant.models import Menu, Booking
from restaurant.serializers import MenuSerializer, BookingSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(name="Icecream", price=80.00, inventory=100)
        Menu.objects.create(name="Pizza", price=200.00, inventory=50)
        Menu.objects.create(name="Burger", price=100.00, inventory=70)

    def test_get_all(self):
        response = self.client.get("/restaurant/menu")
        self.assertEqual(response.status_code, 200)
        serializer = MenuSerializer(Menu.objects.all(), many=True)
        self.assertEqual(response.data['results'], serializer.data)
