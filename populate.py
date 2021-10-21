import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("./iot_telemetry_data.csv")

engine_prod = create_engine("postgresql://admin:password@172.17.0.1:5432/prod")

df[:1000].to_sql("telemetry", con=engine_prod, if_exists="append")

engine_ml = create_engine("postgresql://admin:password@172.17.0.1:5433/ml")

df[:1].to_sql("telemetry", con=engine_ml)
