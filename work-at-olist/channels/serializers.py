from rest_framework import serializers
from rest_framework_nested.relations import NestedHyperlinkedRelatedField

from .models import Channel


class ChannelListSerializer(serializers.ModelSerializer):
    """
    Serializer for channel data
    """
    url = serializers.HyperlinkedIdentityField(
        view_name='api:channel-detail',
        lookup_field='slug'
    )
    channel = serializers.StringRelatedField(source='name')

    class Meta:
        model = Channel
        fields = ('channel', 'url')


class ChannelDetailSerializer(serializers.ModelSerializer):
    """
    Serializer used to show channels detail
    """
    channel = serializers.StringRelatedField(source='name')

    categories = NestedHyperlinkedRelatedField(
        view_name='api:category-detail',
        lookup_field='slug',
        read_only=True,
        many=True,
        parent_lookup_kwargs={'channel_slug': 'channel__slug'}
    )

    class Meta:
        model = Channel
        fields = ('channel', 'categories')
