"""Train and test data sets."""

import pandas as pd
from dagster import AssetOut, AutoMaterializePolicy, multi_asset
from sklearn.model_selection import train_test_split

from ames_housing.constants import RANDOM_STATE


@multi_asset(
    outs={
        "train_data": AssetOut(
            io_manager_key="csv_io_manager",
            auto_materialize_policy=AutoMaterializePolicy.eager(),
        ),
        "test_data": AssetOut(
            io_manager_key="csv_io_manager",
            auto_materialize_policy=AutoMaterializePolicy.eager(),
        ),
    },
)
def train_test_data(
    ames_housing_features: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Train and test data set."""
    train_data, test_data = train_test_split(
        ames_housing_features, random_state=RANDOM_STATE
    )
    return train_data, test_data
