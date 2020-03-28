import pandas as pd
import os
from pathlib import Path

swiss_data = pd.DataFrame()
directory = Path(__file__).parent
for filename in os.listdir(directory / "covid19-cases-switzerland"):
    if filename.endswith("openzh.csv"):
        df = pd.read_csv(os.path.join(directory, filename)).set_index("Date")
        df.columns = [filename[8:-22] + str(col) for col in df.columns]
        swiss_data = pd.concat([swiss_data, df], axis=1)

    else:
        continue

swiss_data.to_csv("swiss_data.csv", index=False)