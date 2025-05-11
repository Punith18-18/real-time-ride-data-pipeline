import pandas as pd
from sqlalchemy import create_engine

# Replace with your actual PostgreSQL password (escape special characters like @ = %40)
db_password = 'Punith%402809'

engine = create_engine(f'postgresql+psycopg2://postgres:{db_password}@localhost:5432/rides_db')

df = pd.read_csv('ride_data.csv')
df.to_sql('ride_data', engine, if_exists='append', index=False)

print("✅ Data loaded successfully into PostgreSQL!")
