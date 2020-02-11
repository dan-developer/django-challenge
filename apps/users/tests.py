from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from apps.financial.models import Transaction
from apps.financial.serializers import TransactionSerializer


class UserTest(TestCase):
    """
    Test for user API
    """

    def test_create_user(self):
        response = self.client.post(reverse('users:user-list'), {
            'username': 'dan',
            'first_name': 'Anderson',
            'last_name': 'Scouto da Silva',
            'password': 'top_secret',
            'phone': '+5551997196110'
        })

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get('username'), 'dan')
        self.assertEqual(response.data.get('is_superuser'), True)
        self.assertEqual(response.data.get('password'), None)

    def test_update_user(self):
        response = self.client.post(reverse('users:user-list'), {
            'username': 'dan',
            'first_name': 'Anderson',
            'last_name': 'Scouto da Silva',
            'password': 'top_secret',
            'phone': '+5551997196111'
        }, content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get('username'), 'dan')
        self.assertEqual(response.data.get('is_superuser'), True)
        self.assertEqual(response.data.get('password'), None)

        response = self.client.put(reverse('users:user-detail', args=[response.data.get('id')]), {
            'username': 'dan',
            'first_name': 'Anderson',
            'last_name': 'Scouto da Silva',
            'password': 'top_secret',
            'phone': '+5551997196111'
        }, content_type='application/json')

        self.assertEqual(response.data.get('username'), 'dan')
        self.assertEqual(response.data.get('phone'), '+5551997196111')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update_user(self):
        response = self.client.post(reverse('users:user-list'), {
            'username': 'dan',
            'first_name': 'Anderson',
            'last_name': 'Scouto da Silva',
            'password': 'top_secret',
            'phone': '+5551997196111'
        }, content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get('username'), 'dan')
        self.assertEqual(response.data.get('is_superuser'), True)
        self.assertEqual(response.data.get('password'), None)

        response = self.client.patch(reverse('users:user-detail', args=[response.data.get('id')]), {
            'username': 'dan_another_user',
        }, content_type='application/json')

        self.assertEqual(response.data.get('username'), 'dan_another_user')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_user(self):
        response = self.client.post(reverse('users:user-list'), {
            'username': 'dan',
            'first_name': 'Anderson',
            'last_name': 'Scouto da Silva',
            'password': 'top_secret',
            'phone': '+5551997196111'
        }, content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get('username'), 'dan')
        self.assertEqual(response.data.get('is_superuser'), True)
        self.assertEqual(response.data.get('password'), None)

        response = self.client.delete(reverse('users:user-detail', args=[response.data.get('id')]))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_not_found_user(self):
        response = self.client.get(reverse('users:user-detail', args=[99999]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

