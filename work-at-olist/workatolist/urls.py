from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^api/', include('core.urls', namespace='api')),
    url(r'^admin/', admin.site.urls),
]
