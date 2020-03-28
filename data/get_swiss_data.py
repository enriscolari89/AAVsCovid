import pandas as pd
import os

directory = r'C:\Users\ENRISCOL\AAVsCovid\data\covid19-cases-switzerland'

swiss_data = pd.DataFrame()
for filename in os.listdir(directory):
    if filename.endswith("openzh.csv"):
        df = pd.read_csv(os.path.join(directory, filename)).set_index("Date")
        df.columns = [filename[8:-22] + str(col) for col in df.columns]
        swiss_data = pd.concat([swiss_data, df], axis=1)

    else:
        continue

swiss_data.to_csv("swiss_data.csv")