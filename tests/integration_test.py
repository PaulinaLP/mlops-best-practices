from datetime import datetime
import pandas as pd

def dt(hour, minute, second=0):
    return datetime(2023, 1, 1, hour, minute, second)

input_file = 's3://nyc-duration/in/2023-01.parquet'

options = {
        'client_kwargs': {
            'endpoint_url': 'http://localhost:4566',  # Localstack endpoint
            'region_name': 'us-east-1',  # Region can be any valid AWS region
        }
    }

# Create a sample dataframe
data = [
    (None, None, dt(1, 1), dt(1, 10)),
    (1, 1, dt(1, 2), dt(1, 10)),
    (1, None, dt(1, 2, 0), dt(1, 2, 59)),
    (3, 4, dt(1, 2, 0), dt(2, 2, 1)),      
    ]

columns = ['PULocationID', 'DOLocationID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime']
df_input = pd.DataFrame(data, columns=columns)

df_input.to_parquet(
    input_file,
    engine='pyarrow',
    compression=None,
    index=False,
    storage_options=options
)   

