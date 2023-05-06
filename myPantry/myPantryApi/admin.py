from django.contrib import admin

from myPantryApi.models import PantryItemCategory, PantryItem, Recipe, Ingredient, ShoppingListItem

class PantryItemCategoryAdmin(admin.ModelAdmin):
    pass
class PantryItemAdmin(admin.ModelAdmin):
    pass
class RecipeAdmin(admin.ModelAdmin):
    pass
class IngredientAdmin(admin.ModelAdmin):
    pass
class ShoppingListItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(PantryItemCategory, PantryItemCategoryAdmin)
admin.site.register(PantryItem, PantryItemAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(ShoppingListItem, ShoppingListItemAdmin)
