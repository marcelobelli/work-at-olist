from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from rest_framework_nested.relations import NestedHyperlinkedIdentityField

from .models import Category


class CategorySimpleSerializer(serializers.ModelSerializer):
    """
        Simple Serializer for category data
    """
    category = serializers.StringRelatedField(source='name')

    url = NestedHyperlinkedIdentityField(
        view_name='api:category-detail',
        lookup_field='slug',
        read_only=True,
        parent_lookup_kwargs={'channel_slug': 'channel__slug'}
    )

    class Meta:
        model = Category
        fields = ('category', 'url')


class ChildrenSerializer(CategorySimpleSerializer):
    """
        Serializer for category children data
    """
    children = serializers.ListSerializer(child=RecursiveField())

    class Meta:
        model = Category
        fields = ('category', 'url', 'children')


class ParentSerializer(CategorySimpleSerializer):
    """
        Serializer for category parent data
    """
    parent = RecursiveField()

    class Meta:

        model = Category
        fields = ('category', 'url', 'parent')


class CategorySerializer(serializers.ModelSerializer):
    """
        Serializer for category data details
    """
    category = serializers.StringRelatedField(source='name')
    children = serializers.ListSerializer(
        child=RecursiveField('ChildrenSerializer')
    )
    parent = ParentSerializer()

    class Meta:
        model = Category
        fields = (
            'category',
            'children',
            'parent',
        )
