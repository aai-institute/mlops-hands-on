"""CSV IO manager."""

from typing import Union

import pandas as pd
from dagster import ConfigurableIOManager, InputContext, OutputContext


def get_path(context: Union[OutputContext, InputContext]) -> str:
    return "data/" + "/".join(context.asset_key.path) + ".csv"
