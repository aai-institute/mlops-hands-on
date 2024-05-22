# Step 3: IO management

## Define the CSV IO manager

```python
class CSVIOManager(ConfigurableIOManager):
    def handle_output(self, context: OutputContext, obj: pd.DataFrame) -> None:
        ...
    def load_input(self, context: InputContext) -> pd.DataFrame:
        ...
```

```python
  def handle_output(self, context: OutputContext, obj: pd.DataFrame) -> None:
      path = get_path(context)
      obj.to_csv(path)
```

```python
  def load_input(self, context: InputContext) -> pd.DataFrame:
      path = get_path(context)
      return pd.read_csv(path)
```



## Register the IO manager

```python

from ames_housing.io_managers.csv_io_manager import CSVIOManager

definitions = Definitions(
    ...
    resources={
        "csv_io_manager": CSVIOManager(),
    },
)
```


## Set the IO manager key on the assets

```python
@asset(io_manager_key="csv_io_manager")
```

```python
@multi_asset(
    outs={
        "train_data": AssetOut(io_manager_key="csv_io_manager"),
        "test_data": AssetOut(io_manager_key="csv_io_manager"),
    }
)
```
