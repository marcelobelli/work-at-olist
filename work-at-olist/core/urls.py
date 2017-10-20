from rest_framework_nested import routers

from django.conf.urls import include, url

from categories.views import CategoryViewSet
from channels.views import ChannelViewSet
from .views import APIRootView

router = routers.SimpleRouter()
router.register(r'channels', ChannelViewSet)

channel_router = routers.NestedSimpleRouter(router, r'channels', lookup='channel')
channel_router.register(r'categories', CategoryViewSet, base_name='category')

urlpatterns = [
    url(r'^$', APIRootView.as_view(), name='root'),
    url(r'^', include(router.urls)),
    url(r'^', include(channel_router.urls)),
]

urlpatterns += router.urls
