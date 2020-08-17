from django.contrib import admin

from .models import Alcohol, Category, Drink, DrinkIngredient, Ingredient, Instruction, Glassware, Technique

class InstructionInline(admin.TabularInline):
    model = Instruction
    extra = 1

class DrinkIngredientInline(admin.TabularInline):
    model = DrinkIngredient
    extra = 1

class DrinkAdmin(admin.ModelAdmin):
    inlines = [InstructionInline, DrinkIngredientInline]
    class Meta:
        model = Drink

admin.site.register(Drink, DrinkAdmin)
admin.site.register(Alcohol)
admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(Glassware)
admin.site.register(Technique)
