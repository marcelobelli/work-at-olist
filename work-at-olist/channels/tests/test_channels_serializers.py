from django.test import TestCase
from model_mommy import mommy

from ..models import Channel
from ..serializers import ChannelDetailSerializer, ChannelListSerializer


class TestChannelListSerializer(TestCase):

    def setUp(self):
        self.channel = mommy.make(Channel)

    def test_channellist_fields(self):
        """ChannelListSerializer must have the fields: name"""
        serializer = ChannelListSerializer(self.channel)
        result = set(serializer.data.keys())
        expected_result = {'name'}

        self.assertEqual(result, expected_result)

    def test_channeldetail_fields(self):
        """ChannelDetailSerializer must have the fields: name"""
        serializer = ChannelDetailSerializer(self.channel)
        result = set(serializer.data.keys())
        expected_result = {'name'}

        self.assertEqual(result, expected_result)
