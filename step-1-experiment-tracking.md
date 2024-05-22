# Step 1: Experiment tracking


## Install MLflow

```
$ pip install mlflow
```


## Import MLflow

```python
import mlflow  
```


## Define the MLflow tracking server and experiment

```python
MLFLOW_TRACKING_SERVER = "http://localhost:5000"
MLFLOW_EXPERIMENT = "ames-housing"
```


## Configure MLflow

```python
mlflow.set_tracking_uri(MLFLOW_TRACKING_SERVER)
mlflow.set_experiment(MLFLOW_EXPERIMENT)
```


## Enable autologging

```python
mlflow.sklearn.autolog()
```


## Wrap fit() and score()

```python
with mlflow.start_run():
    pipeline.fit(train_input, train_output)
    pipeline.score(test_input, test_output)
```
