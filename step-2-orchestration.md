# Step 2: Orchestration

## Install dagster

```
$ pip install dagster dagster-webserver
```

## Define raw data set asset

```python
@asset()
def ames_housing_data() -> pd.DataFrame:
    """Ames housing data set"""
    return pd.read_csv(DATA_SET_URL)
```


## Test/run the asset locally

```python
if __name__ == "__main__":
    raw_data = ames_housing_data()
    print(raw_data.head())
```

```
$ python src/ames_housing/assets/ames_housing_data.py
```


## Register raw data set asset definition
```python
from ames_housing.assets.ames_housing_data import ames_housing_data

definitions = Definitions(
    assets=[
        ames_housing_data,
    ]
)
```


## Define features asset

```python
@asset()
def ames_housing_features(ames_housing_data: pd.DataFrame) -> pd.DataFrame:
    """Ames housing features."""
    columns = (
        FEATURES["nominal"] + FEATURES["ordinal"] + FEATURES["numerical"] + [TARGET]
    )

    return ames_housing_data[columns]
```

```
$ python src/ames_housing/assets/ames_housing_features.py
```


## Test/run the features asset locally

```python
if __name__ == "__main__":
    raw_data = pd.read_csv("data/ames_housing.csv")
    features = ames_housing_features(raw_data)

    print(features.head())
```


## Register the features asset

```python
from ames_housing.assets.ames_housing_features import ames_housing_features

definitions = Definitions(
    assets=[
        ...
        ames_housing_features,
    ]
)
```


## Define the train and test data assets

```python
@multi_asset(
    outs={
        "train_data": AssetOut(),
        "test_data": AssetOut(),
    }
)
def train_test_data(
    ames_housing_features: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Train and test data set."""
    train_data, test_data = train_test_split(
        ames_housing_features, random_state=RANDOM_STATE
    )
    return train_data, test_data
```


## Register train and test data assets

```python
from ames_housing.assets.train_test import train_test_data

definitions = Definitions(
    assets=[
        ...
        train_test_data,
    ]
)
```


## Define model asset

```python
from ames_housing.assets.price_prediction_model import price_prediction_model

definitions = Definitions(
    assets=[
        ...
        price_prediction_model,
    ]
)
```
