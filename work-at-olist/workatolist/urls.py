from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView
from django.urls import reverse_lazy

urlpatterns = [
    url(r'^$', RedirectView.as_view(url=reverse_lazy('api:root'))),
    url(r'^api/', include('core.urls', namespace='api')),
    url(r'^admin/', admin.site.urls),
]
