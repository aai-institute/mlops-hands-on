"""Ames housing data set."""

import pandas as pd
from dagster import AutoMaterializePolicy, AutoMaterializeRule, asset

from ames_housing.constants import DATA_SET_URL

