from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from channels.serializers import ChannelListSerializer
from .models import Category


class ChildrenSerializer(serializers.ModelSerializer):
    """
        Serializer for category children data
    """
    category = serializers.StringRelatedField(source='name')
    children = serializers.ListSerializer(child=RecursiveField())

    url = serializers.HyperlinkedIdentityField(
        view_name='api:category-detail',
        lookup_field='slug'
    )

    class Meta:
        model = Category
        fields = ('category', 'url', 'children')


class ParentSerializer(serializers.ModelSerializer):
    """
        Serializer for category parent data
    """
    category = serializers.StringRelatedField(source='name')
    parent = RecursiveField()

    url = serializers.HyperlinkedIdentityField(
        view_name='api:category-detail',
        lookup_field='slug'
    )

    class Meta:

        model = Category
        fields = ('category', 'url', 'parent')



class CategorySerializer(serializers.ModelSerializer):
    """
        Serializer for category data
    """
    category = serializers.StringRelatedField(source='name')
    children = serializers.ListSerializer(child=RecursiveField('ChildrenSerializer'))
    channel = ChannelListSerializer()
    parent = ParentSerializer()

    url = serializers.HyperlinkedIdentityField(
        view_name='api:category-detail',
        lookup_field='slug'
    )

    class Meta:
        model = Category
        fields = (
            'category',
            'url',
            'children',
            'parent',
            'channel'
        )
