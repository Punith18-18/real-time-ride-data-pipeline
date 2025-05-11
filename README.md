# real-time-ride-data-pipeline
Simulated ride-hailing pipeline with Python, PostgreSQL &amp; Power BI
# 🚕 Real-Time Ride Data Pipeline Project

This project simulates ride-hailing data (like Uber), loads it into a PostgreSQL database using Python, and visualizes it in Power BI.

---

## 📌 Overview

This end-to-end data pipeline demonstrates how to:

- Generate realistic ride data using Python and Faker
- Export the data to a CSV file
- Load the CSV into a PostgreSQL database using SQLAlchemy
- Build an interactive dashboard using Power BI

---

## 🛠 Tools & Tech Stack

| Purpose           | Technology         |
|------------------|--------------------|
| Data Generation   | Python, Faker       |
| Data Handling     | Pandas, CSV         |
| Database          | PostgreSQL          |
| Data Ingestion    | SQLAlchemy, psycopg2|
| Visualization     | Power BI            |

---

## 📁 Project Structure

```
real-time-ride-data-pipeline/
├── ride_data_generator.py     # Python script to generate ride data
├── load_to_postgres.py        # Script to insert data into PostgreSQL
├── ride_data.csv              # Generated dataset (example)
├── requirements.txt           # Python dependencies
└── README.md                  # Project overview and instructions
```

---

## 📊 Dashboard Highlights

The Power BI dashboard includes:

- Pie chart showing ride status breakdown (completed, cancelled, ongoing)
- Stacked bar chart of rides per pickup area by status
- Line chart tracking rides over time
- KPI cards for total rides, total revenue, and average distance
- Slicers for filtering by ride status or city

---

## 🧠 Key Learnings

- How to simulate and automate realistic datasets
- Setting up and interacting with PostgreSQL using Python
- Using SQLAlchemy for efficient database operations
- Building a clean, interactive Power BI dashboard
- Translating raw data into business insights

---

## 🚀 How to Run This Project

1. **Generate data**  
   Run `ride_data_generator.py` to create a CSV file with simulated rides.

2. **Load data into PostgreSQL**  
   Ensure PostgreSQL is installed and running. Then run `load_to_postgres.py` to insert the data into your database.

3. **Connect Power BI**  
   - Open Power BI Desktop  
   - Connect to PostgreSQL using the `localhost` and `rides_db`  
   - Load `ride_data` table and start building your visuals
