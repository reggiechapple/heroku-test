import uuid
from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify

class Alcohol(models.Model):
    slug = models.SlugField(max_length=128, unique=True, blank=True)
    name = models.CharField(max_length=100, unique=True, blank=True)

    class Meta:
        verbose_name = "alcohol"
        verbose_name_plural = "alcohols"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("alcohol_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Glassware(models.Model):

    slug = models.SlugField(max_length=128, unique=True, blank=True)
    name = models.CharField(max_length=100, unique=True, blank=True)
    icon = models.ImageField(upload_to='photos/glassware/%Y/%m/%d/', null=True, blank=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    alt_text = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "glassware"
        verbose_name_plural = "glassware"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("glassware_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Category(models.Model):
    slug = models.SlugField(max_length=128, unique=True, blank=True)
    name = models.CharField(max_length=100, unique=True, blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Technique(models.Model):
    slug = models.SlugField(max_length=128, unique=True, blank=True)
    name = models.CharField(max_length=100, unique=True, blank=True)

    class Meta:
        verbose_name = "technique"
        verbose_name_plural = "techniques"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("technique_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Ingredient(models.Model):

    slug = models.SlugField(max_length=128, unique=True, blank=True)
    name = models.CharField(max_length=100, unique=True, blank=True)

    class Meta:
        verbose_name = "ingredient"
        verbose_name_plural = "ingredients"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ingredient_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Drink(models.Model):

    slug = models.SlugField(max_length=128, unique=True, blank=True)
    name = models.CharField(max_length=100, unique=True, blank=True)
    photo = models.ImageField(upload_to='photos/drinks/%Y/%m/%d/', null=True, blank=True)
    technique = models.ForeignKey(Technique, on_delete=models.SET_NULL, related_name='drinks', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='drinks', null=True, blank=True)
    alcohols = models.ManyToManyField(Alcohol, related_name='drinks', blank=True)
    glassware = models.ManyToManyField(Glassware, related_name='drinks', blank=True)

    class Meta:
        verbose_name = "drink"
        verbose_name_plural = "drinks"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("drinks:drink_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_alcohols(self):
        return Alcohol.objects.all()
    
    def get_glassware(self):
        return Glassware.objects.all()

    def get_techniques(self):
        return Technique.objects.all()

class Instruction(models.Model):
    step = models.CharField(max_length=255, blank=True, null=True)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE, related_name="instructions")

    class Meta:
        verbose_name = "instruction"
        verbose_name_plural = "instructions"

    def __str__(self):
        return self.step

class DrinkIngredient(models.Model):

    amount = models.CharField(max_length=50, blank=True, null=True)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='drinks', blank=True)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE, related_name='ingredients', blank=True)

    class Meta:
        verbose_name = "drink ingredient"
        verbose_name_plural = "drink ingredients"