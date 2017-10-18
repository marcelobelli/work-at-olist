from django.test import TestCase

from channels.models import Channel
from ..models import Category


class ChannelModelTest(TestCase):

    def test_slug_creation(self):
        """slug must be created automatically after category creation"""
        channel = Channel.objects.create(**{'name': 'Big Market'})
        category = Category.objects.create(**{'name': 'Video game', 'channel': channel})

        self.assertTrue(category.slug)
