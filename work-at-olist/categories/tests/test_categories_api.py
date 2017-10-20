from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase

from channels.models import Channel

from ..models import Category
from ..serializers import CategorySerializer


class CategoryListAPI(APITestCase):

    def setUp(self):
        self.channel = Channel.objects.create(**{'name': 'Big Market'})
        self.url = reverse(
            'api:category-list',
            kwargs={'channel_slug': self.channel.slug}
        )

    def test_get_response_from_category_list(self):
        """GET method must return 200"""
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_data_from_category_list(self):
        """Must return all categories from db"""
        factory = APIRequestFactory()
        request = factory.get(self.url)


        for category in ['Video Game', 'Computers', 'Smartphones']:
            cat_dict = {'name': category, 'channel': self.channel}
            Category.objects.create(**cat_dict)

        categories = Category.objects.all()
        serializer = CategorySerializer(
            categories,
            many=True,
            context={'request': request}
        )

        response = self.client.get(self.url)

        self.assertEqual(response.data['results'], serializer.data)


class CategoryDetailAPI(APITestCase):

    def setUp(self):
        channel = Channel.objects.create(**{'name': 'Big Market'})
        cat_dict = {'name': 'Video game', 'channel': channel}
        self.category = Category.objects.create(**cat_dict)
        self.url = reverse(
            'api:category-detail',
            kwargs={'channel_slug': channel.slug, 'slug': self.category.slug}
        )

    def test_get_response_from_category_detail(self):
        """GET method must return 200"""
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_data_from_category_detail(self):
        """Must return category from db"""
        factory = APIRequestFactory()
        request = factory.get(self.url)

        serializer = CategorySerializer(
            self.category,
            context={'request': request}
        )

        response = self.client.get(self.url)

        self.assertEqual(response.data, serializer.data)
