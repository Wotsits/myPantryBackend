import uuid
from django.db import models

# Models which create the database tables for the API.

class PantryItemCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=False, null=False)
    icon = models.CharField(max_length=100, unique=False, null=False, default="question")

    def __str__(self):
        return self.name

class PantryItem(models.Model):

    #####################
    # ENUMS for field value.

    class CapacityMeasure(models.TextChoices):
        ML = "ml"
        G = "g"
        ITEM = "item"

    class Containers(models.TextChoices):
        CAN = "can"
        TUBE = "tube"
        JAR = "jar"
        PACK = "pack"
        BLOCK = "block"
        BOTTLE = "bottle"
        ITEM = "item"
        
    ######################

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=False, null=False)
    capacity = models.PositiveSmallIntegerField(null=False, default=1)
    capacityMeasure = models.CharField(max_length=255, null=False, choices=CapacityMeasure.choices, default=CapacityMeasure.ITEM)
    container = models.CharField(max_length=255, null=False, choices=Containers.choices, default=Containers.ITEM)
    on_hand = models.DecimalField(decimal_places=2, max_digits=20, null=False, default=1)
    category = models.ForeignKey(PantryItemCategory, null=False, on_delete=models.CASCADE)
    imageSrc = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=False, null=False)
    imageSrc = models.URLField(null=True, blank=True)
    serves = models.PositiveSmallIntegerField(null=False, default=2)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    recipe = models.ForeignKey(Recipe, null=False, on_delete=models.CASCADE)
    pantryItem = models.ForeignKey(PantryItem, null=False, on_delete=models.CASCADE)
    quantity = models.DecimalField(decimal_places=2, max_digits=20, default=1)

    def __str__(self):
        return self.recipe.name + "-" + self.pantryItem.name + "-" + str(self.quantity)
    
class ShoppingListItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    quantity = models.DecimalField(decimal_places=2, max_digits=20, default=1)
    pantryItem = models.ForeignKey(PantryItem, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.pantryItem.name + "-" + str(self.quantity)
