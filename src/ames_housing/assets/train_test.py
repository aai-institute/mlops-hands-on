"""Train and test data sets."""

import pandas as pd
from dagster import AssetOut, AutomationCondition, multi_asset
from sklearn.model_selection import train_test_split

from ames_housing.constants import RANDOM_STATE
