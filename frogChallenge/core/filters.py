from django.db.models.functions import Greatest
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
        valid_choices = {'proteins', 'carbohydrates', 'fats'}
        if value not in valid_choices:
            return queryset

        fields_to_compare = valid_choices - {value}
        return queryset.filter(**{f"{value}__gt": Greatest(*fields_to_compare)})

