from rest_framework import serializers

from core.models import Channel, Category


class ChannelSerializer(serializers.ModelSerializer):
    channel = serializers.CharField(source='name')

    class Meta:
        model = Channel
        fields = ('channel',)


class CategoryListSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='name')
    children = serializers.StringRelatedField(many=True)

    class Meta:
        model = Category
        fields = ('category', 'level', 'children')


class CategoryFamilySerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='name')

    class Meta:
        model = Category
        fields = ('category', 'level', 'id')
