from rest_framework import serializers
from category.models import Category, LANGUAGE_CHOICES, STYLE_CHOICES

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description')
