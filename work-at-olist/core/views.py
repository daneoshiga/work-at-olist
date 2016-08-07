from rest_framework import mixins
from rest_framework import generics

from core.models import Channel, Category
from core.serializers import (ChannelSerializer, CategoryListSerializer,
                              CategoryFamilySerializer)


class ChannelList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CategoryList(mixins.ListModelMixin, generics.GenericAPIView):
    serializer_class = CategoryListSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        channel = self.kwargs.get('channel')
        return (Category.objects
                .filter(channel=channel)
                .filter(level=0))


class CategoryFamily(mixins.ListModelMixin, generics.GenericAPIView):
    serializer_class = CategoryFamilySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        pk = self.kwargs.get('category_id')
        return (Category.objects
                .get(pk=pk)
                .get_family())
