from rest_framework import serializers

from core.models import Category, Channel


class ChannelSerializer(serializers.ModelSerializer):
    """Serialize channel data"""
    channel = serializers.CharField(source='name')

    class Meta:
        model = Channel
        fields = ('id', 'channel',)


class CategoryListSerializer(serializers.ModelSerializer):
    """Serialize the categories tree with parents and children"""

    def to_representation(self, instance):
        return instance.serializable_tree()


class CategoryFamilySerializer(serializers.ModelSerializer):
    """Serialize a category 'family', the category with its parents and
    subcategories
    """
    category = serializers.CharField(source='name')

    class Meta:
        model = Category
        fields = ('id', 'category')
