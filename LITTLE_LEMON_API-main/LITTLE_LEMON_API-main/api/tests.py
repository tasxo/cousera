from django.test import TestCase
from .models import Menu, Booking
from django.contrib.auth.models import User

class SimpleTests(TestCase):
    def test_create_menu(self):
        m = Menu.objects.create(title='Test', price=9.99, inventory=5)
        self.assertEqual(str(m), 'Test')

    def test_create_booking(self):
        b = Booking.objects.create(name='Ram', guests=2, date='2025-01-01')
        self.assertIn('Ram', str(b))
