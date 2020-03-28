import pandas as pd
import json
from pathlib import Path


def load_geo_distribution(country_to_keep=["AUT", "CHE", "CHN", "DEU", "ESP", "FRA", "GBR", "ITA", "USA"]):
    with open(Path("data/geo_repartition.json"), "r") as f:
        geo_repartition = json.load(f)
    df = pd.json_normalize(geo_repartition["records"])
    df = df.rename(columns={"dateRep": "datetime"})
    df["datetime"] = pd.to_datetime(df["datetime"], format="%d/%m/%Y")
    df = df[df["countryterritoryCode"].isin(country_to_keep)]
    df["cases"] = df["cases"].astype(int)
    df["deaths"] = df["deaths"].astype(int)
    df["popData2018"] = df["popData2018"].astype(int)
    df = (df.rename(columns={"countryterritoryCode": "country_code", "popData2018": "tot_pop_2018"})
          .drop(columns=["day", "month", "year", "countriesAndTerritories", "geoId"])
          .reset_index(drop=True)
          )
    return df


if __name__ == "__main__":
    load_geo_distribution()
