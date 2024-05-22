"""Ames housing price prediction model training pipeline."""

from dagster import Definitions

from ames_housing.assets.ames_housing_data import ames_housing_data
from ames_housing.assets.ames_housing_features import ames_housing_features
from ames_housing.assets.price_prediction_model import price_prediction_model
from ames_housing.assets.train_test import train_test_data
from ames_housing.io_managers.csv_io_manager import CSVIOManager
from ames_housing.resources.training_config import ModelTrainingConfig

definitions = Definitions(
    assets=[
        ames_housing_data,
        ames_housing_features,
        train_test_data,
        price_prediction_model,
    ],
    resources={
        "csv_io_manager": CSVIOManager(),
        "train_config": ModelTrainingConfig(
            learning_rate=0.1,
            n_estimators=100,
            random_state=42,
        )
    },
)
