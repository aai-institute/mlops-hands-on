"""Ames housing price prediction model training pipeline."""

from dagster import (
    AssetSelection,
    DefaultScheduleStatus,
    Definitions,
    ScheduleDefinition,
)

definitions = Definitions(
    assets=[],
    resources={},
)
