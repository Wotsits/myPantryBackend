
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view
from myPantryApi.serializers import UserSerializer, GroupSerializer, PantryItemSerializer, PantryItemCategorySerializer, RecipeSerializer, IngredientSerializer, IngredientSerializerCreate, ShoppingListItemSerializer, PantryItemSerializerCreate
from myPantryApi.models import PantryItem, PantryItemCategory, Recipe, Ingredient, ShoppingListItem
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from decimal import Decimal
import math

# -------------------------
# Pantry Item Views
# -------------------------

@api_view(['GET', 'POST'])
def pantryItemList(request):
    # GET: Return all pantry items
    if request.method == 'GET':
        pantryItems = PantryItem.objects.all()
        serializer = PantryItemSerializer(pantryItems, many=True)
        return Response(serializer.data)
    # POST: Create a new pantry item
    if request.method == 'POST':
        serializer = PantryItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_422_UNPROCESSABLE)

@api_view(['GET', 'PUT', 'DELETE'])
def pantryItemDetail(request, id):
    try: 
        pantryItem = PantryItem.objects.get(id=id)
    except PantryItem.DoesNotExist: 
        return Response(status.HTTP_404_NOT_FOUND)
    # GET: Return pantry item by id
    if request.method == "GET":
        serializer = PantryItemSerializer(pantryItem)
        return Response(serializer.data)
    # PUT: Update pantry item by id
    elif request.method == "PUT": 
        serializer = PantryItemSerializerCreate(pantryItem, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    # DELETE: Delete pantry item by id
    elif request.method == "DELETE": 
        pantryItem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST']) 
def newPantryItem(request):
    # POST: Create a new pantry item
    if request.method == "POST":
        serializer = PantryItemSerializerCreate(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

@api_view(['GET', 'POST'])
def pantryItemCategoryList(request):
    # GET: Return all pantry item categories
    if request.method == 'GET':
        pantryItemCategories = PantryItemCategory.objects.all()
        serializer = PantryItemCategorySerializer(pantryItemCategories, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def pantryItemsByCategory(request, categoryId):
    # GET: Return all pantry items by category
    if request.method == 'GET':
        try: 
            pantryItems = PantryItem.objects.filter(category=categoryId)
        except PantryItem.DoesNotExist: 
            return Response(status.HTTP_404_NOT_FOUND)
        
        serializer = PantryItemSerializer(pantryItems, many=True)
        return Response(serializer.data)

# -------------------------
# Recipe Views
# -------------------------
        
@api_view(['GET'])
def recipeList(request):
    # GET: Return all recipes
    if request.method == 'GET':
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def recipeDetail(request, id):
    try: 
        recipeItem = Recipe.objects.get(id=id)
    except Recipe.DoesNotExist: 
        return Response(status.HTTP_404_NOT_FOUND)
    
    # GET: Return recipe by id
    if request.method == "GET":
        serializer = RecipeSerializer(recipeItem)
        return Response(serializer.data)
    # PUT: Update recipe by id
    elif request.method == "PUT": 
        serializer = RecipeSerializer(recipeItem, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    # DELETE: Delete recipe by id
    elif request.method == "DELETE": 
        recipeItem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['POST'])
def newRecipe(request):
    # POST: Create a new recipe
    if request.method == "POST":
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

@api_view(['GET'])
def ingredientsByRecipe(request, recipeId):
    # GET: Return all ingredients by recipeId
    if request.method == 'GET':
        try: 
            ingredients = Ingredient.objects.filter(recipe=recipeId)
        except Ingredient.DoesNotExist: 
            return Response(status.HTTP_404_NOT_FOUND)
        serializer = IngredientSerializer(ingredients, many=True)
        return Response(serializer.data)
    
@api_view(['GET', 'PUT', 'DELETE'])
def ingredientDetail(request, ingredientId):
    print(ingredientId)
    # GET: Return an ingredient
    if request.method == 'GET':
        ingredient = Ingredient.objects.get(id=ingredientId)
        serializer = IngredientSerializer(ingredient)
        return Response(serializer.data)
    # PUT: Update an ingredient
    if request.method == 'PUT':
        ingredient = Ingredient.objects.get(id=ingredientId)
        serializer = IngredientSerializerCreate(ingredient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    # DELETE: Delete an ingredient
    if request.method == 'DELETE':
        
        ingredient = Ingredient.objects.get(id=ingredientId)
        ingredient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def newIngredient(request):
    # POST: Create a new ingredient
    if request.method == 'POST':
        serializer = IngredientSerializerCreate(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

# -------------------------
# Shopping List Views
# -------------------------

@api_view(['POST'])
def generateShoppingList(request):
    # POST: Generate a shopping list
    if request.method == 'POST':
        # get the recipes from the request
        recipes = request.data
        # create an array to hold the ingredients needed
        ingredientsNeeded = []
        # loop through the recipes and get the ingredients for each recipe
        for recipe in recipes:
            # get the servings required for the recipe
            recipeServingsRequired = recipe['servings']
            # get the recipe from the database
            recipeObj = Recipe.objects.get(id=recipe['id'])
            # get the recipe servings from the database object
            recipeServes = recipeObj.serves
            # get the ingredients for the recipe
            recipeIngredients = list(Ingredient.objects.filter(recipe=recipe['id']))
            # loop through the ingredients and add them to the ingredientsNeeded array
            for recipeIngredient in recipeIngredients:
                multiplier = recipeServingsRequired / recipeServes
                quantity = recipeIngredient.quantity * Decimal(multiplier)
                ingredientsNeeded.append({"ingredient": recipeIngredient, "quantity": quantity})
            print(ingredientsNeeded)
        # consolidate the ingredients needed so that any duplicates can be consolidated into one ingredient
        consolidatedIngredients = []
        for ingredient in ingredientsNeeded:
            # check if the ingredient is already in the consolidatedIngredients array as a value to the pantryItem key on one of the objects
            indexInArray = -1
            if len(consolidatedIngredients) != 0:
                for index, consolidatedIngredient in enumerate(consolidatedIngredients):
                    if consolidatedIngredient['pantryItem'].id == ingredient['ingredient'].pantryItem.id:
                        indexInArray = index
            # if the ingredient is already in the array, add the quantity of the ingredient to the quantity of the ingredient in the consolidatedIngredients array
            if indexInArray != -1:
                # add the quantity of the ingredient to the quantity of the ingredient in the consolidatedIngredients array
                consolidatedIngredients[indexInArray]['quantity'] += ingredient['quantity']
            else:
                #  add an object to the consolidatedIngredients array which is the pantryItem and the quantity needed
                consolidatedIngredients.append({
                    'pantryItem': ingredient['ingredient'].pantryItem,
                    'quantity': ingredient['quantity']
                })
        #  We now have a list of consolidated ingredients needed for the recipes
        #  We need to compare this list to the pantry items and see if we have enough of each ingredient
        #  If we have enough of an ingredient, we don't need to add it to the shopping list
        #  If we don't have enough of an ingredient, we need to add the quantity needed to the shopping list

        #  create an array to hold the shopping list items
        shortfall = []
        #  analyse the shortcomings of the pantry
        for pantryItem in consolidatedIngredients:
            #  get the pantry item from the database
            pantryItemObj = PantryItem.objects.get(id=pantryItem['pantryItem'].id)
            #  check if the quantity of the pantry item is greater than the quantity needed
            if pantryItemObj.on_hand < pantryItem['quantity']:
                #  add the shortfall to the shortfall array
                shortfall.append({
                    'pantryItem': pantryItemObj,
                    'quantity': math.ceil(pantryItem['quantity'] - pantryItemObj.on_hand)
                })
        # add each item in the shortfall array to the shopping list
        for item in shortfall:
            # create a shopping list item
            shoppingListItem = ShoppingListItem(pantryItem=item['pantryItem'], quantity=item['quantity'])
            # save the shopping list item
            shoppingListItem.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def shoppingListItems(request):
    # GET: Return all shopping list items
    if request.method == 'GET':
        shoppingListItems = ShoppingListItem.objects.all()
        serializer = ShoppingListItemSerializer(shoppingListItems, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def addShoppingListItemsToPantry(request):
    # POST: Add shopping list items to the pantry
    if request.method == 'POST':
        # get the shopping list items from the request
        shoppingListItems = request.data
        # loop through the shopping list items and add them to the pantry
        for shoppingListItem in shoppingListItems:
            # get the pantry item from the database
            pantryItem = PantryItem.objects.get(id=shoppingListItem['item']['pantryItem']['id'])
            # add the quantity to the pantry item
            pantryItem.on_hand += Decimal(shoppingListItem['item']['quantity'])
            # save the pantry item
            pantryItem.save()
            # delete the shopping list item
            ShoppingListItem.objects.get(id=shoppingListItem['item']['id']).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# -------------------------
# Consume Recipes Views
# -------------------------

@api_view(['POST'])
def consumeRecipes(request):
    # POST: Consume the ingredients for the recipes
    if request.method == "POST":
        # get the recipes from the request
        recipes = request.data
        # loop through the recipes and consume the ingredients
        for recipe in recipes:
            # get the recipe from the database
            recipeObj = Recipe.objects.get(id=recipe['id'])
            # get the recipe servings from the database object
            recipeServes = recipeObj.serves
            # get the ingredients for the recipe
            recipeIngredients = list(Ingredient.objects.filter(recipe=recipe['id']))
            # loop through the ingredients and add them to the ingredientsNeeded array
            for recipeIngredient in recipeIngredients:
                # get the pantry item from the database
                pantryItem = PantryItem.objects.get(id=recipeIngredient.pantryItem.id)
                # get the quantity of the ingredient needed
                quantityNeeded = recipeIngredient.quantity * Decimal(recipe['servings'] / recipeServes)
                # consume the quantity of the ingredient
                pantryItem.on_hand -= quantityNeeded
                # save the pantry item
                pantryItem.save()
        return Response(status=status.HTTP_204_NO_CONTENT)