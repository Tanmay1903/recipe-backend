from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Name must be at least 3 characters long.")
        return value

    def validate_ingredients(self, value):
        if not value:
            raise serializers.ValidationError("Ingredients cannot be empty.")
        return value

    def validate_steps(self, value):
        if not value:
            raise serializers.ValidationError("Steps cannot be empty.")
        return value