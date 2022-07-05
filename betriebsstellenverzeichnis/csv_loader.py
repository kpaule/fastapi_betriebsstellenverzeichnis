import pandas as pd

from .database import engine


def load_csv(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        col_names = ["plc", "rl100_code", "rl100_name", "rl100_name_short", "type_short", "type",
                     "operating_status", "start_date", "end_date", "branch", "regional_area", "last_modified"]
        data = pd.read_csv(file, sep=";", header=None,
                           skiprows=1, names=col_names)
    data.to_sql("betriebsstelle", con=engine, index=True,
                index_label="id", if_exists="replace")
