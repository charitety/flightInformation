import psycopg2
import pandas as pd
import numpy as np
from config import params


# connecting
conn = psycopg2.connect(**params)

# cursor connection
cursor = conn.cursor()
#selecting rows of flights that were not cancelled nor diverted
cursor.execute("SELECT * FROM real_flight WHERE cancelled = '0' and diverted = '0';") 
rows = cursor.fetchall()
cursor.close()

#print(rows)

# dataframe creation
df = pd.DataFrame(rows, columns=[desc.name for desc in cursor.description])
#verifying if the data was filtered adequately 
print(df[df['diverted'] == "1"])
print(df[df['cancelled'] == "1"])

# checking if we have null values to deternine if we need to clean the data (dropna)
missingRowsDeparture = df[df["dep_del15"].isna()]
print(len(missingRowsDeparture))

missingRowsArrival = df[df["arr_del15"].isna()]
print(len(missingRowsArrival))

# creating a new column 
# group by airlines & get average

# group by origin airports & get average