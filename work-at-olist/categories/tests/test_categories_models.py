from django.test import TestCase

from channels.models import Channel
from ..models import Category


class ChannelModelTest(TestCase):
    def setUp(self):
        self.channel = Channel.objects.create(**{'name': 'Big Market'})
        self.categories = ['Video Game', 'Playstation 4']

    def test_slug_creation(self):
        """slug must be created automatically after category creation"""

        category = Category.objects.create(**{'name': 'Video game', 'channel': self.channel})

        self.assertTrue(category.slug)

    def test_import_categories_method(self):
        """Method must imports categories from a list to given channel"""
        Category.import_categories(self.channel, self.categories)

        result = Category.objects.count()

        self.assertEqual(result, len(self.categories))

    def test_import_categories_parent_children_relationship(self):
        """In a list, the first category must be the parent of the second"""
        Category.import_categories(self.channel, self.categories)

        parent = Category.objects.get(name=self.categories[0])
        children = Category.objects.get(name=self.categories[1])

        self.assertEqual(parent, children.parent)
