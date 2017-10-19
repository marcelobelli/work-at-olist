from django.urls import reverse
from rest_framework.test import APIRequestFactory, APITestCase

from channels.models import Channel
from ..models import Category
from ..serializers import CategorySerializer, ChildrenSerializer, ParentSerializer


class TestCategorySerializer(APITestCase):

    def setUp(self):
        factory = APIRequestFactory()
        url = reverse('api:category-list')
        channel = Channel.objects.create(**{'name': 'Big Market'})

        self.request = factory.get(url)
        self.category = Category.objects.create(**{'name': 'Video game', 'channel': channel})

    def test_categoryserializer_fields(self):
        """CategorySerializer must have the fields: category, url, children, parent, channel"""
        serializer = CategorySerializer(self.category, context={'request': self.request})
        result = set(serializer.data.keys())
        expected_result = {
            'category',
            'url',
            'children',
            'parent',
            'channel'
        }

        self.assertEqual(result, expected_result)

    def test_childrenserializer_fields(self):
        """ChildrenSerializer must have the fields: category, url, children"""
        serializer = ChildrenSerializer(self.category, context={'request': self.request})
        result = set(serializer.data.keys())
        expected_result = {
            'category',
            'url',
            'children',
        }

        self.assertEqual(result, expected_result)

    def test_parentserializer_fields(self):
        """ParentSerializer must have the fields: category, url, parent"""
        serializer = ParentSerializer(self.category, context={'request': self.request})
        result = set(serializer.data.keys())
        expected_result = {
            'category',
            'url',
            'parent',
        }

        self.assertEqual(result, expected_result)
