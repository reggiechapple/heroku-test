from django.contrib import admin

from .models import Alcohol, Category, Drink, DrinkIngredient, Ingredient, Instruction, Glassware, Technique

class InstructionInline(admin.TabularInline):
    model = Instruction
    extra = 1

class DrinkIngredientInline(admin.TabularInline):
    model = DrinkIngredient
    extra = 1

class DrinkAdmin(admin.ModelAdmin):
    inlines = [DrinkIngredientInline, InstructionInline]
    ordering = ['name',]

    class Meta:
        model = Drink

class AlcoholAdmin(admin.ModelAdmin):
    ordering = ['name',]
    
    class Meta:
        model = Alcohol

class CategoryAdmin(admin.ModelAdmin):
    ordering = ['name',]
    
    class Meta:
        model = Category

class IngredientAdmin(admin.ModelAdmin):
    ordering = ['name',]
    
    class Meta:
        model = Ingredient

class GlasswareAdmin(admin.ModelAdmin):
    ordering = ['name',]
    
    class Meta:
        model = Glassware

class TechniqueAdmin(admin.ModelAdmin):
    ordering = ['name',]
    
    class Meta:
        model = Technique

admin.site.register(Drink, DrinkAdmin)
admin.site.register(Alcohol, AlcoholAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Glassware, GlasswareAdmin)
admin.site.register(Technique, TechniqueAdmin)
