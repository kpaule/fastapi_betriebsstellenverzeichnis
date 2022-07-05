from pydantic import BaseSettings


class Settings(BaseSettings):
    csv_name: str = "DBNetz-Betriebsstellenverzeichnis-Stand2021-10.csv"