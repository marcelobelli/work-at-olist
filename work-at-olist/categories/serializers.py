from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from channels.serializers import ChannelListSerializer
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    """
        Serializer for category data
    """
    category = serializers.StringRelatedField(source='name')
    children = serializers.ListSerializer(child=RecursiveField())

    url = serializers.HyperlinkedIdentityField(
        view_name='api:category-detail',
        lookup_field='slug'
    )

    channel = ChannelListSerializer()
    
    class Meta:
        model = Category
        fields = (
            'category',
            'url',
            'children',
            'parent',
            'channel'
        )
