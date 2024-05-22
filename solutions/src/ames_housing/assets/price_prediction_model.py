"""Price prediction model."""

import mlflow
import pandas as pd
from dagster import AutoMaterializePolicy, asset
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler

from ames_housing.constants import (
    FEATURES,
    MLFLOW_EXPERIMENT,
    MLFLOW_TRACKING_SERVER,
    RANDOM_STATE,
    TARGET,
)
from ames_housing.resources.training_config import ModelTrainingConfig


@asset(auto_materialize_policy=AutoMaterializePolicy.eager())
def price_prediction_model(
    train_config: ModelTrainingConfig, train_data: pd.DataFrame, test_data: pd.DataFrame
) -> None:
    """Price prediction model."""

    # Split train and test features and target
    train_input = train_data.drop([TARGET], axis=1)
    train_output = train_data[TARGET]

    test_input = test_data.drop([TARGET], axis=1)
    test_output = test_data[TARGET]

    # Ordinal pipeline
    ordinal_pipeline = Pipeline(
        [
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("encoder", OrdinalEncoder()),
        ]
    )

    # Nominal pipeline
    nominal_pipeline = Pipeline(
        [
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("encoder", OneHotEncoder(handle_unknown="ignore")),
        ]
    )

    # Numerical pipeline
    numerical_pipeline = Pipeline(
        [
            ("imputer", SimpleImputer(strategy="mean")),
            ("encoder", StandardScaler()),
        ]
    )

    # Preprocessing
    preprocessing_pipeline = ColumnTransformer(
        [
            ("ordinal_preprocessor", ordinal_pipeline, FEATURES["ordinal"]),
            ("nominal_preprocessor", nominal_pipeline, FEATURES["nominal"]),
            ("numerical_preprocessor", numerical_pipeline, FEATURES["numerical"]),
        ]
    )

    # Estimator
    pipeline = Pipeline(
        [
            ("preprocessor", preprocessing_pipeline),
            (
                "estimator",
                GradientBoostingRegressor(
                    learning_rate=train_config.learning_rate,
                    n_estimators=train_config.n_estimators,
                    random_state=train_config.random_state,
                ),
            ),
        ]
    )

    # Configure mlflow
    mlflow.set_tracking_uri(MLFLOW_TRACKING_SERVER)
    mlflow.set_experiment(MLFLOW_EXPERIMENT)

    # Enable the autologger
    mlflow.sklearn.autolog()

    # Fit and score the pipeline
    with mlflow.start_run():
        pipeline.fit(train_input, train_output)
        pipeline.score(test_input, test_output)
