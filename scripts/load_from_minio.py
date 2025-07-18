from minio import Minio
import pandas as pd
from io import BytesIO

print("⏳ Connecting to MinIO...")
client = Minio(
    "minio:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False
)

print("📥 Downloading 'sales.csv' from bucket 'raw'")
data = client.get_object("raw", "sales.csv")
df = pd.read_csv(BytesIO(data.read()))
print(f"✅ Downloaded data with shape: {df.shape}")
df.to_csv("/tmp/sales.csv", index=False)
print("📁 Data saved to /tmp/sales.csv")
