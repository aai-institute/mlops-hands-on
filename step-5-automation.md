# Step 5: Automation

## Set the auto materialization policy to CRON for the raw data asset

```python
@asset(
    io_manager_key="csv_io_manager",
    auto_materialize_policy=AutoMaterializePolicy.eager().with_rules(
        AutoMaterializeRule.materialize_on_cron("*/2 * * * *")
    ),
)
```

```python
@asset(
    io_manager_key="csv_io_manager",
    auto_materialize_policy=AutoMaterializePolicy.eager(),
)
```

```python
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
```

```python
@asset(auto_materialize_policy=AutoMaterializePolicy.eager())
```
