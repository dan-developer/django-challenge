from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from apps.financial.models import Transaction
from apps.financial.serializers import TransactionSerializer


class TransactionTest(TestCase):
    """
    Test for transaction API
    """

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='Dan', email='and.dan19@gmail.com', password='super_secret_password'
        )
        self.transaction = Transaction.objects.create(
            user=self.user,
            type=Transaction.TYPE_IN,
            value=25487451.45
        )

    def test_validate_single_transaction(self):
        response = self.client.get(reverse('financial:transaction-detail', args=[self.transaction.pk]))
        transaction = Transaction.objects.get(pk=self.transaction.pk)
        serializer = TransactionSerializer(transaction)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(float(response.data.get('value')), 25487451.45)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_transaction(self):
        response = self.client.post(reverse('financial:transaction-list'), {
            'user': self.user.pk,
            'value': 459.7,
            'type': 2
        })
        self.assertEqual(float(response.data.get('value')), 459.7)
        self.assertEqual(int(response.data.get('type')), 2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_transaction(self):
        response = self.client.post(reverse('financial:transaction-list'), {
            'user': self.user.pk,
            'value': 459.7,
            'type': 2
        })
        self.assertEqual(float(response.data.get('value')), 459.7)
        self.assertEqual(int(response.data.get('type')), 2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        pk = response.data.get('id')

        response = self.client.put(reverse('financial:transaction-detail', args=[pk]), {
            'user': self.user.pk,
            'value': 559.7,
            'type': 2
        }, content_type='application/json')

        self.assertEqual(float(response.data.get('value')), 559.7)
        self.assertEqual(int(response.data.get('type')), 2)
        self.assertEqual(pk, response.data.get('id'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update_transaction(self):
        response = self.client.post(reverse('financial:transaction-list'), {
            'user': self.user.pk,
            'value': 98774,
            'type': 1
        })
        self.assertEqual(float(response.data.get('value')), 98774)
        self.assertEqual(int(response.data.get('type')), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        pk = response.data.get('id')

        response = self.client.patch(reverse('financial:transaction-detail', args=[pk]), {
            'value': 98775,
        }, content_type='application/json')

        self.assertEqual(float(response.data.get('value')), 98775)
        self.assertEqual(int(response.data.get('type')), 1)
        self.assertEqual(pk, response.data.get('id'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_delete_transaction(self):
        response = self.client.post(reverse('financial:transaction-list'), {
            'user': self.user.pk,
            'value': 98774,
            'type': 1
        })
        self.assertEqual(float(response.data.get('value')), 98774)
        self.assertEqual(int(response.data.get('type')), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        pk = response.data.get('id')

        response = self.client.delete(reverse('financial:transaction-detail', args=[pk]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_not_found_transaction(self):
        response = self.client.get(reverse('financial:transaction-detail', args=[99999]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
