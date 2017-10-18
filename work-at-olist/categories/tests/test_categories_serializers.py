from django.test import TestCase
from channels.models import Channel

from ..models import Category
from ..serializers import CategorySerializer


class TestCategorySerializer(TestCase):

    def test_category_fields(self):
        channel = Channel.objects.create(**{'name': 'Big Market'})
        category = Category.objects.create(**{'name': 'Video game', 'channel': channel})
        serializer = CategorySerializer(category)
        result = set(serializer.data.keys())
        expected_result = {
            'name',
            'channel',
            'parent',
            'children'
        }

        self.assertEqual(result, expected_result)
