from django.conf.urls import url

from core import views

urlpatterns = [
    url(r'^channels/$', views.ChannelList.as_view()),
    url(r'^channel/(?P<channel>[a-z0-9-]+)/$', views.CategoryList.as_view()),
    url(r'^category/(?P<category_id>[a-z0-9-]+)/$',
        views.CategoryFamily.as_view()),
]
