import pandas as pd
import psycopg2

print("📤 Loading data from /tmp/sales.csv to PostgreSQL...")
df = pd.read_csv("/tmp/sales.csv")
print(f"📊 Read DataFrame with shape: {df.shape}")

conn = psycopg2.connect(
    dbname="airflow",
    user="airflow",
    password="airflow",
    host="postgres",
    port=5432
)
cursor = conn.cursor()

print("🛠️ Creating table if not exists...")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales_staging (
        order_id INT,
        product_id INT,
        customer_id TEXT,
        quantity INT,
        total_price NUMERIC,
        order_date DATE
    );
""")

print("📥 Inserting rows into sales_staging table...")
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO sales_staging VALUES (%s, %s, %s, %s, %s, %s);
    """, tuple(row))
conn.commit()
cursor.close()
conn.close()
print("✅ Data inserted successfully into PostgreSQL.")
