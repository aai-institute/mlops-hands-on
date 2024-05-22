"""Ames housing features."""

import pandas as pd
from dagster import AutoMaterializePolicy, asset

from ames_housing.constants import FEATURES, TARGET


@asset(
    io_manager_key="csv_io_manager",
    auto_materialize_policy=AutoMaterializePolicy.eager(),
)
def ames_housing_features(ames_housing_data: pd.DataFrame) -> pd.DataFrame:
    """Ames housing features."""
    columns = (
        FEATURES["nominal"] + FEATURES["ordinal"] + FEATURES["numerical"] + [TARGET]
    )

    return ames_housing_data[columns]


if __name__ == "__main__":
    raw_data = pd.read_csv("data/ames_housing.csv")
    features = ames_housing_features(raw_data)

    print(features.head())
