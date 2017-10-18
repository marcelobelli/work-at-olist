from rest_framework import serializers

from .models import Channel


class ChannelListSerializer(serializers.ModelSerializer):
    """
    Serializer for channel data
    """
    class Meta:
        model = Channel
        fields = ('name', )


class ChannelDetailSerializer(serializers.ModelSerializer):
    """
    Serializer used to show channels detail
    """
    class Meta:
        model = Channel
        fields = ('name', )
