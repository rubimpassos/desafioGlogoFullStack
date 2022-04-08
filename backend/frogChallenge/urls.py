from django.contrib import admin
from django.urls import path

from .core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/foods/', views.FoodAPIListView.as_view(), name='food-api-list'),
]
