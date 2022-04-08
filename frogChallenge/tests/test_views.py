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


@pytest.mark.parametrize(
    'filter_kind, expected_food_names',
    [
        ('proteins', {'Pancake de carne moída', 'Salmão Grelhado'}),
        ('carbohydrates', {'Macarrão cozido', 'Arroz cozido'}),
        ('fats', {'Óleo de coco'}),
    ]
)
def test_api_list_greatest_food_values(client, filter_kind, expected_food_names):
    Food.objects.bulk_create(
        [
            Food(
                name='Macarrão cozido',
                quantity=100,
                proteins=5,
                carbohydrates=22,
                fats=5,
            ),
            Food(
                name='Salmão Grelhado',
                quantity=100,
                proteins=52,
                carbohydrates=2,
                fats=5,
            ),
            Food(
                name='Arroz cozido',
                quantity=100,
                proteins=5,
                carbohydrates=12,
                fats=5,
            ),
            Food(
                name='Pancake de carne moída',
                quantity=100,
                proteins=52,
                carbohydrates=2,
                fats=5,
            ),
            Food(
                name='Óleo de coco',
                quantity=100,
                proteins=3,
                carbohydrates=2,
                fats=54,
            ),
        ]
    )

    response = client.get(f'/api/foods/?greatest={filter_kind}')

    returned_food_names = {food['name'] for food in response.json()}
    assert returned_food_names == expected_food_names
