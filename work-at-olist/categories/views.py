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
