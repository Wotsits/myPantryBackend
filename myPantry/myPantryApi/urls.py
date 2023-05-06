from django.urls import include, path
from . import views


urlpatterns = [
    path('pantryItems/', views.pantryItemList),
    path('pantryItem/<str:id>', views.pantryItemDetail),
    path('newPantryItem/', views.newPantryItem),
    path('pantryItemCategories/', views.pantryItemCategoryList),
    path('pantryItemsByCategory/<str:categoryId>', views.pantryItemsByCategory),

    path('recipes/', views.recipeList),
    path('recipe/<str:id>', views.recipeDetail),
    path('newRecipe/', views.newRecipe),
    path('ingredientsByRecipe/<str:recipeId>', views.ingredientsByRecipe),
    path('ingredient/<str:ingredientId>', views.ingredientDetail),
    path('newIngredient/', views.newIngredient),

    path('generateShoppingList/', views.generateShoppingList),
    path('shoppingListItems/', views.shoppingListItems),
    path('addShoppingListItemsToPantry/', views.addShoppingListItemsToPantry), 
    path('consumeRecipes/', views.consumeRecipes)

]