from django.db.models import Q
from django.shortcuts import render

from .models import Drink

def all_drinks(request):
    template_name = 'drinks/list.html'
    context = {}
    drinks = Drink.objects.all().order_by('name')
    search_term = ''
    if 'q' in request.GET:
        search_term = request.GET['q']
        drinks = drinks.filter(
            Q(name__icontains=search_term) |
            Q(category__name__icontains=search_term) |
            Q(instructions__step__icontains=search_term)).distinct().order_by('name')
    context["drinks"] = drinks
    return render(request, template_name, context)

def drink_detail(request, slug):
    template_name = 'drinks/detail.html'
    context = {}
    drink = Drink.objects.get(slug=slug)
    context["drink"] = drink
    return render(request, template_name, context)