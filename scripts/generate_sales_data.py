import pandas as pd
import random
from faker import Faker

fake = Faker()
data = []

for _ in range(10000):
    data.append({
        'order_id': random.randint(100000, 999999),
        'product_id': random.randint(1, 100),
        'customer_id': fake.uuid4(),
        'quantity': random.randint(1, 5),
        'total_price': round(random.uniform(10.0, 500.0), 2),
        'order_date': fake.date_between(start_date='-6M', end_date='today')
    })

df = pd.DataFrame(data)
df.to_csv("sales.csv", index=False)
