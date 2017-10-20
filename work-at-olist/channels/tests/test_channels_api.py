from model_mommy import mommy
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase

from django.urls import reverse

from ..models import Channel
from ..serializers import ChannelDetailSerializer, ChannelListSerializer


class ChannelsListAPITest(APITestCase):

    def setUp(self):
        self.url = reverse('api:channel-list')

    def test_get_response_from_channel_list(self):
        """GET method must return 200"""
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_data_from_channel_list(self):
        """Must return all channels from db"""
        for _ in range(5):
            mommy.make(Channel)

        factory = APIRequestFactory()
        request = factory.get(self.url)

        channels = Channel.objects.all()
        serializer = ChannelListSerializer(
            channels, many=True,
            context={'request': request}
        )

        response = self.client.get(self.url)

        self.assertEqual(response.data['results'], serializer.data)


class ChannelsDetailAPITest(APITestCase):

    def setUp(self):
        self.channel = mommy.make(Channel)
        self.url = reverse(
            'api:channel-detail',
            kwargs={'slug': self.channel.slug}
        )

    def test_get_response_from_channel_detail(self):
        """GET method must return 200"""
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_data_from_channel_detail(self):
        """Must return channel from db"""
        serializer = ChannelDetailSerializer(self.channel)

        response = self.client.get(self.url)

        self.assertEqual(response.data, serializer.data)
