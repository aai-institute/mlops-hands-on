"""CSV IO manager."""

from typing import Union

import pandas as pd
from dagster import ConfigurableIOManager, InputContext, OutputContext


def get_path(context: Union[OutputContext, InputContext]) -> str:
    return "data/" + "/".join(context.asset_key.path) + ".csv"


class CSVIOManager(ConfigurableIOManager):
    def handle_output(self, context: OutputContext, obj: pd.DataFrame) -> None:
        path = get_path(context)
        obj.to_csv(path)

    def load_input(self, context: InputContext) -> pd.DataFrame:
        path = get_path(context)
        return pd.read_csv(path)
