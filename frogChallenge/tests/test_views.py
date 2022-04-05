import pytest
from pytest_unordered import unordered

from ..core.models import Food

pytestmark = pytest.mark.django_db


def test_api_list_foods(client):
    foods = [
        Food.objects.create(
            name='Apple',
            quantity=1,
            proteins=2,
            carbohydrates=3,
            fats=4,
        ),
        Food.objects.create(
            name='Banana',
            quantity=4,
            proteins=5,
            carbohydrates=6,
            fats=7,
        )
    ]

    response = client.get('/api/foods/')
    assert response.status_code == 200
    assert response.json() == unordered([
        {
            'id': food.id,
            'name': food.name,
            'quantity': food.quantity,
            'proteins': food.proteins,
            'carbohydrates': food.carbohydrates,
            'fats': food.fats,
        } for food in foods
    ])
