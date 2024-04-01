import unittest
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class ProfileTestCase(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'password'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_profile_page(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Profile')

    def test_edit_profile(self):
        self.client.login(username=self.username, password=self.password)
        data = {'first_name': 'John', 'last_name': 'Doe', 'email': 'john@example.com'}
        response = self.client.post(reverse('edit_profile'), data)
        self.assertEqual(response.status_code, 302)