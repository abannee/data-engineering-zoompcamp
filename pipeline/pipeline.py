import sys
import pandas as pd

print('arguments',sys.argv)

month = int(sys.argv[1])

# sys.argv[0] is always the name of the script (pipeline.py).

# sys.argv[1] is the first argument you provide after the filename.

df = pd.DataFrame({"day": [1, 2], "num_passengers": [3, 4]})
df['month'] = month
print(df.head())

df.to_parquet(f"output_{month}.parquet")


print(f'hello pipeline, month={month}')