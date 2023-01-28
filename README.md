This program analyzes historic data of flights and calculates delays that occured in a month.

The data was retrieved from this kaggle page: https://www.kaggle.com/datasets/divyansh22/flight-delay-prediction?select=Jan_2020_ontime.csv and imported to postgresql.

The process was as follows:
-Rows were pulled from a postgresql database using psycopg2 for flights that were not diverted nor cancelled.
-A data exploration was performed to determine if there were Null values in the corresponding columns for arrival delays and departure delays.
-Average (ratio) of delayed flights for each airline and each airport are generated.
