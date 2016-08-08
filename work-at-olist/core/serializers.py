from rest_framework import serializers

from core.models import Channel, Category


class ChannelSerializer(serializers.ModelSerializer):
    """Serialize channel data"""
    channel = serializers.CharField(source='name')

    class Meta:
        model = Channel
        fields = ('id', 'channel',)


class CategoryListSerializer(serializers.ModelSerializer):
    """Serialize the categories tree with parents and children"""
    category = serializers.CharField(source='name')

    class Meta:
        model = Category
        fields = ('id', 'category', 'children')

    def get_fields(self):
        fields = super().get_fields()
        fields['children'] = CategoryListSerializer(many=True)
        return fields


class CategoryFamilySerializer(serializers.ModelSerializer):
    """Serialize a category 'family', the category with its parents and
    subcategories
    """
    category = serializers.CharField(source='name')

    class Meta:
        model = Category
        fields = ('id', 'category')
