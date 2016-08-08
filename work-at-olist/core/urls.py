from django.conf.urls import url

from core import views

urlpatterns = [
    url(r'^channels/$', views.ChannelList.as_view(), name='channel_list'),
    url(r'^channel/(?P<channel>[a-z0-9-]+)/$', views.CategoryList.as_view(),
        name='category_list'),
    url(r'^category/(?P<category_id>[a-z0-9-]+)/$',
        views.CategoryFamily.as_view(), name='category_family'),
]
