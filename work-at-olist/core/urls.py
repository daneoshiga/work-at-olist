from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from core import views

urlpatterns = [
    url(r'^channels/$', views.ChannelList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
