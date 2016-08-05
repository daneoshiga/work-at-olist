from rest_framework import serializers

from core.models import Channel


class ChannelSerializer(serializers.ModelSerializer):
    channel = serializers.CharField(source='name')

    class Meta:
        model = Channel
        fields = ('channel',)
