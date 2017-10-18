from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Channel
from .serializers import ChannelDetailSerializer, ChannelListSerializer


class ChannelViewSet(ReadOnlyModelViewSet):
    """
    Viewset used to show channels list and detail
    """
    lookup_field = 'slug'
    queryset = Channel.objects.all()

    def get_serializer_class(self):
        serializers = {
            'list': ChannelListSerializer,
            'retrieve': ChannelDetailSerializer,
        }
        return serializers[self.action]
