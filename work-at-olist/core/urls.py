from rest_framework import routers

from categories.views import CategoryViewSet
from channels.views import ChannelViewSet

router = routers.SimpleRouter()
router.register(r'channels', ChannelViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = router.urls
