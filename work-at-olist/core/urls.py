from rest_framework import routers

from django.conf.urls import include, url

from categories.views import CategoryViewSet
from channels.views import ChannelViewSet
from .views import APIRootView

router = routers.SimpleRouter()
router.register(r'channels', ChannelViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    url(r'^$', APIRootView.as_view(), name='root'),
]

urlpatterns += router.urls
