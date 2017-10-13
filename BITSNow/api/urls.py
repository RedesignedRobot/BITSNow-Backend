from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ItemView,ItemCreateView

urlpatterns = {
    url(r'^api/$', ItemView.as_view(), name="view"),
    url(r'^api/create/$', ItemCreateView.as_view(), name="create"),
    url(r'^api/destroy/$', ItemCreateView.as_view(), name="destroy"),
}

urlpatterns = format_suffix_patterns(urlpatterns)