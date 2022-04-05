from django.db.models import Max
from django_filters import ChoiceFilter
from django_filters.rest_framework import FilterSet

from .models import Food


class FoodFilter(FilterSet):
    greatest = ChoiceFilter(
        choices=[
            ('proteins', 'Proteínas'),
            ('carbohydrates', 'Carboidratos'),
            ('fats', 'Gorduras'),
        ],
        method='filter_greatest',
    )

    class Meta:
        model = Food
        fields = ['greatest']

    def filter_greatest(self, queryset, name, value):
        max_field_value = queryset.aggregate(max=Max(value))['max']
        return queryset.filter(**{value: max_field_value})
