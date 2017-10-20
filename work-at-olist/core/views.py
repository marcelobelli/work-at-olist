import json

from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.reverse import reverse


class APIRootView(APIView):

    def get(self, request):
        data = {
            'url': reverse('api:channel-list', request=request),
            'description': 'Show all Channels',
        }

        return Response(data)
