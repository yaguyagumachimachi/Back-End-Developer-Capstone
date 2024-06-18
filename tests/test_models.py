from django.test import TestCase
from restaurant.models import Menu, Booking


class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(
            Title="IceCream", Price=80.12, Inventory=100)
        self.assertEqual(str(item), 'IceCream : 80.12')


class BookingTest(TestCase):
    def test_get_item(self):
        item = Booking.objects.create(
            Name="Test Client", No_of_guests=5, BookingDate='2024-06-24')
        print(str(item))
        self.assertEqual(str(item), 'Test Client : 5 : 2024-06-24')
