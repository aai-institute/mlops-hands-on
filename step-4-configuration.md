# Step 4: Configuration

## Define the resource

```python
class ModelTrainingConfig(ConfigurableResource):
    """Model training configuration"""

    learning_rate: float
    n_estimators: int
    random_state: int
```


## Load the config in the asset

```python
@asset()
def price_prediction_model(
    train_config: ModelTrainingConfig, train_data: pd.DataFrame, test_data: pd.DataFrame
) -> None:
    """Price prediction model."""
```

```python
GradientBoostingRegressor(
    learning_rate=train_config.learning_rate,
    n_estimators=train_config.n_estimators,
    random_state=train_config.random_state,
),
```


## Register the training config

```python
from ames_housing.resources.training_config import ModelTrainingConfig

definitions = Definitions(
    ...
    resources={
        ...
        "train_config": ModelTrainingConfig(
            learning_rate=0.1,
            n_estimators=100,
            random_state=42,
        ),
    },
)
```
