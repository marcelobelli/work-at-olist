from rest_framework import serializers

from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    """
        Serializer for category data
    """
    class Meta:
        model = Category
        fields = (
            'name',
            'channel',
            'parent',
            'children'
        )
