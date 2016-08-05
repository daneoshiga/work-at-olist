from rest_framework import mixins
from rest_framework import generics

from core.models import Channel
from core.serializers import ChannelSerializer


class ChannelList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
