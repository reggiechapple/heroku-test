from django.urls import path, include

from . import views

urlpatterns = [
    path('drinks/', include(([
        path('', views.all_drinks, name='all_drinks'),
        path('<slug:slug>/', views.drink_detail, name='drink_detail'),
    ], 'drinks'))),
]