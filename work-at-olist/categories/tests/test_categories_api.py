from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from channels.models import Channel

from ..models import Category
from ..serializers import CategorySerializer


class CategoryListAPI(APITestCase):

    def setUp(self):
        self.url = reverse('api:category-list')

    def test_get_response_from_category_list(self):
        """GET method must return 200"""
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_data_from_category_list(self):
        """Must return all categories from db"""
        channel = Channel.objects.create(**{'name': 'Big Market'})
        for category in ['Video Game', 'Computers', 'Smartphones']:
            Category.objects.create(**{'name': category, 'channel': channel})

        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)

        response = self.client.get(self.url)

        self.assertEqual(response.data, serializer.data)


class CategoryDetailAPI(APITestCase):

    def setUp(self):
        channel = Channel.objects.create(**{'name': 'Big Market'})
        self.category = Category.objects.create(**{'name': 'Video game', 'channel': channel})
        self.url = reverse('api:category-detail', kwargs={'slug': self.category.slug})

    def test_get_response_from_category_detail(self):
        """GET method must return 200"""
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_data_from_category_detail(self):
        """Must return category from db"""
        serializer = CategorySerializer(self.category)

        response = self.client.get(self.url)

        self.assertEqual(response.data, serializer.data)