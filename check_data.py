import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://admin:password@172.17.0.1:5433/ml")

print(engine.execute("SELECT COUNT(*) FROM telemetry").first())
