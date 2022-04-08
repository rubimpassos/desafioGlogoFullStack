import re

import pandas as pd
from numpy import float64


def get_foods_from_file(file_path):
    with open(file_path, encoding="utf-8") as f:
        lines = f.readlines()
        data = [
            [col.strip().replace('\n', '') for col in re.split(r"\s{3,}|\t+", line)]
            for line in lines[2:]
        ]

        return pd.DataFrame(
            data,
            columns=["name", "quantity", "proteins", "carbohydrates", "fats"],
            dtype=float64,
        )
