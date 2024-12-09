"""Configuration"""

DATA_SET_URL = "https://raw.githubusercontent.com/janwillemkl/mlops-hands-on/main/data/ames_housing.csv"

FEATURES = {
    "nominal": ["ms_zoning", "lot_shape", "land_contour"],
    "ordinal": ["land_slope", "overall_qual", "overall_cond"],
    "numerical": ["lot_frontage", "lot_area", "mas_vnr_area"],
}
TARGET = "sale_price"

RANDOM_STATE = 42

MLFLOW_TRACKING_SERVER = "http://localhost:4000"
MLFLOW_EXPERIMENT = "ames-housing"
