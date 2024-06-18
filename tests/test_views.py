from django.test import TestCase
from restaurant.views import Menu, Booking
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient


class MenuViewTest(TestCase):

    def setUp(self):
        item = Menu.objects.create(
            Title="IceCream", Price=80.12, Inventory=100)

        # create test user
        self.user = User.objects.create_user(
            username='testuser', password='123@!pass')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()

    def test_menu_getall(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get('http://127.0.0.1:8000/restaurant/menu/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.json(
        )), "[{'id': 2, 'Title': 'IceCream', 'Price': '80.12', 'Inventory': 100}]")


class SingleMenuTest(TestCase):

    def setUp(self):
        item = Menu.objects.create(
            Title="baked egg", Price=3.00, Inventory=100)

        # create test user
        self.user = User.objects.create_user(
            username='testuser', password='123@!pass')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()

    def test_singlemenu_getall(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        get_id = self.client.get(
            'http://127.0.0.1:8000/restaurant/menu/').data[0].get('id')
        response = self.client.get(
            f'http://127.0.0.1:8000/restaurant/menu/{get_id}')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.json(
        )), f"{{'id': {get_id}, 'Title': 'baked egg', 'Price': '3.00', 'Inventory': 100}}")


class BookingViewSetTest(TestCase):

    def setUp(self):
        item = Booking.objects.create(
            Name="Test Client", No_of_guests=5, BookingDate='2024-06-24')

        # create test user
        self.user = User.objects.create_user(
            username='testuser', password='123@!pass')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()

    def test_booking_getall(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get(
            'http://127.0.0.1:8000/restaurant/booking/tables/')
        get_id = response.data[0].get('id')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            str(response.json()),
            f"[{{'id': {get_id}, 'Name': 'Test Client', 'No_of_guests': 5, 'BookingDate': '2024-06-24'}}]")

    def test_single_booking_getall(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        get_id = self.client.get(
            'http://127.0.0.1:8000/restaurant/booking/tables/').data[0].get('id')
        response = self.client.get(
            f'http://127.0.0.1:8000/restaurant/booking/tables/{get_id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.json(
        )), f"{{'id': {get_id}, 'Name': 'Test Client', 'No_of_guests': 5, 'BookingDate': '2024-06-24'}}")
