from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Category
from .serializers import CategorySerializer


class CategoryViewSet(ReadOnlyModelViewSet):
    """
    Viewset used to show categories list and detail
    """
    lookup_field = 'slug'
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def retrieve(self, request, *args, **kwargs):
        channel_slug = kwargs['channel_slug']
        slug = kwargs['slug']
        queryset = Category.objects.filter(
            channel__slug=channel_slug,
            slug=slug
        )
        category = get_object_or_404(queryset)
        serializer = CategorySerializer(category, context={'request': request})

        return Response(serializer.data)
