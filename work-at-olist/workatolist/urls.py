from django.conf.urls import include, url

urlpatterns = [
    url(r'^api/1/', include('core.urls',
                            namespace='core')),
]
