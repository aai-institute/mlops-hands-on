"""Ames housing data set."""

import pandas as pd
from dagster import asset, AutoMaterializePolicy, AutoMaterializeRule

from ames_housing.constants import DATA_SET_URL


@asset(
    io_manager_key="csv_io_manager",
    auto_materialize_policy=AutoMaterializePolicy.eager().with_rules(
        AutoMaterializeRule.materialize_on_cron("*/2 * * * *")
    ),
)
def ames_housing_data() -> pd.DataFrame:
    """Ames housing data set"""
    return pd.read_csv(DATA_SET_URL)


if __name__ == "__main__":
    raw_data = ames_housing_data()
    print(raw_data.head())
