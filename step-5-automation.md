# Step 5: Automation

## Set the auto materialization policy to CRON for the raw data asset

```python
schedule = ScheduleDefinition(
    name="schedule",
    target=AssetSelection.assets(["ames_housing_data"]),
    cron_schedule="*/2 * * * *",
    default_status=DefaultScheduleStatus.RUNNING,
)

definitions = Definitions(
    ...
    schedules=[schedule],
)
```

```python
@asset(
    io_manager_key="csv_io_manager",
    automation_condition=AutomationCondition.eager(),
)
```

```python
@multi_asset(
    outs={
        "train_data": AssetOut(
            io_manager_key="csv_io_manager",
            automation_condition=AutomationCondition.eager(),
        ),
        "test_data": AssetOut(
            io_manager_key="csv_io_manager",
            automation_condition=AutomationCondition.eager(),
        ),
    },
)
```

```python
@asset(automation_condition=AutomationCondition.eager())
```
