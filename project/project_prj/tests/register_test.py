import unittest
from django.test import TestCase
from django.contrib.auth.models import User
from .forms import UserRegisterForm


class RegistrationTestCase(TestCase):

    def test_user_registration_form_valid(self):
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123'
        }
        form = UserRegisterForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_user_registration_form_invalid(self):
        form_data = {
            'username': 'testuser',
            'email': 'invalidemail',
            'password1': 'testpassword123',
            'password2': 'testpassword123'
        }
        form = UserRegisterForm(data=form_data)
        self.assertFalse(form.is_valid())