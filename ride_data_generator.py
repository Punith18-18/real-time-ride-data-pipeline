from faker import Faker
import pandas as pd
import random
import uuid
from datetime import datetime

fake = Faker()

def create_ride():
    ride = {
        "ride_id": str(uuid.uuid4()),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "rider_name": fake.name(),
        "pickup_area": fake.city(),
        "dropoff_area": fake.city(),
        "distance_km": round(random.uniform(1, 20), 2),
        "base_fare": 5.00,
        "final_fare": 0.0,
        "status": random.choice(["completed", "cancelled", "ongoing"])
    }
    ride["final_fare"] = round(ride["base_fare"] + ride["distance_km"] * 1.5, 2)
    return ride

def generate_ride_data(count=50):
    data = [create_ride() for _ in range(count)]
    df = pd.DataFrame(data)
    df.to_csv("ride_data.csv", index=False)
    print("✅ ride_data.csv generated with", count, "rides.")

if __name__ == "__main__":
    generate_ride_data()
