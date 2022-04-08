import os

import pandas as pd
import pytest
from numpy import float64
from pandas._testing import assert_frame_equal

from . import cases
from ..core.food import get_foods_from_file


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
def test_get_foods_from_valid_file(shared_datadir, file_path, expected_data):
    """Precisa retornar os dados do arquivo em um Dataframe"""
    # print os files
    os.listdir(shared_datadir)
    food_df = get_foods_from_file(shared_datadir / file_path)

    assert_frame_equal(food_df, pd.DataFrame(
        expected_data,
        columns=[
            "name", "quantity", "proteins", "carbohydrates", "fats"
        ],
        dtype=float64
    ))


