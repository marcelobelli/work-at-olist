import json

from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.reverse import reverse


class APIRootView(APIView):

    def get(self, request):
        data = {
            'channels': {
                'url': reverse('api:channel-list', request=request),
                'description': 'Show all Channels',
            },
            'categories': {
                'url': reverse('api:category-list', request=request),
                'description': 'Show all Categories',
            },
        }

        return Response(data)
