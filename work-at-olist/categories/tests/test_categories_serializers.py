from django.urls import reverse
from rest_framework.test import APIRequestFactory, APITestCase

from channels.models import Channel
from ..models import Category
from ..serializers import CategorySerializer


class TestCategorySerializer(APITestCase):

    def test_category_fields(self):
        """CategorySerializer must have the fields: category, url, children, parent, channel"""
        factory = APIRequestFactory()
        url = reverse('api:category-list')
        request = factory.get(url)
        channel = Channel.objects.create(**{'name': 'Big Market'})
        category = Category.objects.create(**{'name': 'Video game', 'channel': channel})
        serializer = CategorySerializer(category, context={'request': request})
        result = set(serializer.data.keys())
        expected_result = {
            'category',
            'url',
            'children',
            'parent',
            'channel'
        }

        self.assertEqual(result, expected_result)
