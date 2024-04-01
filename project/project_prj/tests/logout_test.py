import unittest
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class LogoutTestCase(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'password'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_logout(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Logged out')