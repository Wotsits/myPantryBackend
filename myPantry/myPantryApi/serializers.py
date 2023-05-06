from django.contrib.auth.models import User, Group
from rest_framework import serializers
from myPantryApi.models import PantryItem, PantryItemCategory, Recipe, Ingredient, ShoppingListItem

# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class PantryItemCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PantryItemCategory
        fields = '__all__'

# This serializer is used to serialize the pantryItem for read operations.
class PantryItemSerializer(serializers.ModelSerializer):
    category = PantryItemCategorySerializer()

    class Meta:
        model = PantryItem
        fields = ['id', 'name', 'category', 'capacity', 'capacityMeasure', 'container', 'on_hand']
        related_object = 'PantryItemCategory'

# This serializer is used to serialize the pantryItem for create operations.
class PantryItemSerializerCreate(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(many=False, queryset=PantryItemCategory.objects.all())

    class Meta:
        model = PantryItem
        fields = ['id', 'name', 'category', 'capacity', 'capacityMeasure', 'container', 'on_hand']
        related_object = 'PantryItemCategory'

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'

# This serializer is used to serialize the ingredients for read operations.
class IngredientSerializer(serializers.ModelSerializer):
    pantryItem = PantryItemSerializer()
    class Meta:
        model = Ingredient
        fields = ['id', 'pantryItem', 'recipe', 'quantity']
        related_object = 'PantryItem'

# This serializer is used to serialize the ingredients for create operations.
class IngredientSerializerCreate(serializers.ModelSerializer):
    pantryItem = serializers.PrimaryKeyRelatedField(many=False, queryset=PantryItem.objects.all())
    recipe = serializers.PrimaryKeyRelatedField(many=False, queryset=Recipe.objects.all())

    class Meta:
        model = Ingredient
        fields = ['id', 'pantryItem', 'recipe', 'quantity']
        related_object = ['PantryItem', 'Recipe']

class ShoppingListItemSerializer(serializers.ModelSerializer):
    pantryItem = PantryItemSerializer()

    class Meta:
        model = ShoppingListItem
        fields = ['id', 'pantryItem', 'quantity']
        related_object = 'PantryItem'
