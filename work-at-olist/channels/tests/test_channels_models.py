from django.db import IntegrityError
from django.test import TestCase

from ..models import Channel


class ChannelModelTest(TestCase):

    def setUp(self):
        self.name = 'Big Market'
        self.channel = Channel.objects.create(**{'name': self.name})

    def test_slug_creation(self):
        """slug must be created automatically after channel creation"""
        self.assertTrue(self.channel.slug)

    def test_name_duplication(self):
        """Must raise Integrity Error if try to duplicate channel's name"""
        with self.assertRaises(IntegrityError):
            Channel.objects.create(**{'name': self.name})
