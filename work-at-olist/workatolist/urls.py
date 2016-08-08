from django.conf.urls import url, include

urlpatterns = [
    url(r'^api/1/', include('core.urls',
                            namespace='core')),
]
