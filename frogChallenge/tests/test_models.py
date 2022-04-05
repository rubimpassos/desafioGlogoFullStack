import pytest
from django.core.files import File

from . import cases
from ..core.models import Food, ImportedFile

pytestmark = pytest.mark.django_db


@pytest.mark.parametrize("file_path, expected_data", [
    cases.case_01_valid,
    cases.case_02_valid,
    cases.case_03_valid,
    cases.case_04_valid,
    cases.case_05_valid,
    cases.case_06_valid,
    cases.case_07_valid,
    cases.case_08_valid,
    cases.case_09_valid,
])
def test_import_file_after_create_file_record(shared_datadir, file_path, expected_data):
    ImportedFile.objects.create(
        file=File(open(shared_datadir / file_path, "rb"), name=file_path)
    )

    foods = Food.objects.all()

    assert len(foods) == len(expected_data)
    expected_data_by_name = {food[0]: food for food in expected_data}
    for food in foods:
        assert food.name in expected_data_by_name
        assert food.quantity == expected_data_by_name[food.name][1]
        assert food.proteins == expected_data_by_name[food.name][2]
        assert food.carbohydrates == expected_data_by_name[food.name][3]
        assert food.fats == expected_data_by_name[food.name][4]


def test_import_file_after_create_file_record_with_duplicate_name(shared_datadir):
    """Precisa salvar somente o primeiro registro."""
    ImportedFile.objects.create(
        file=File(
            open(shared_datadir / "case_10_duplicate_name.txt", "rb"),
            name="case_10_duplicate_name.txt"
        )
    )

    foods = Food.objects.all()

    assert len(foods) == 1
    assert foods[0].name == "Pasta de soja"
    assert foods[0].quantity == 100.0
    assert foods[0].proteins == 5.0
    assert foods[0].carbohydrates == 22.0
    assert foods[0].fats == 50.0


def test_import_file_after_create_file_record_updates_existing_food(shared_datadir):
    """Precisa salvar somente o primeiro registro."""
    food = Food.objects.create(
        name="Panqueca de carne moída",
        quantity=1.0,
        proteins=1.0,
        carbohydrates=1.0,
        fats=1.0
    )

    ImportedFile.objects.create(
        file=File(
            open(shared_datadir / "case_01.txt", "rb"),
            name="case_01.txt"
        )
    )

    expected_data = cases.case_01_valid[0][1][0]

    food.refresh_from_db()
    assert food.quantity == expected_data[1]
    assert food.proteins == expected_data[2]
    assert food.carbohydrates == expected_data[3]
    assert food.fats == expected_data[4]
