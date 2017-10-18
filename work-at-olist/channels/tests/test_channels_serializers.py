from django.urls import reverse
from model_mommy import mommy
from rest_framework.test import APIRequestFactory, APITestCase

from ..models import Channel
from ..serializers import ChannelDetailSerializer, ChannelListSerializer


class TestChannelListSerializer(APITestCase):

    def setUp(self):
        factory = APIRequestFactory()
        url = reverse('api:channel-list')

        self.request = factory.get(url)
        self.channel = mommy.make(Channel)


    def test_channellist_fields(self):
        """ChannelListSerializer must have the fields: channel, url"""
        serializer = ChannelListSerializer(self.channel, context={'request': self.request})
        result = set(serializer.data.keys())
        expected_result = {'channel', 'url'}

        self.assertEqual(result, expected_result)

    def test_channeldetail_fields(self):
        """ChannelDetailSerializer must have the fields: channel, categories"""
        serializer = ChannelDetailSerializer(self.channel, context={'request': self.request})
        result = set(serializer.data.keys())
        expected_result = {'channel', 'categories'}

        self.assertEqual(result, expected_result)
