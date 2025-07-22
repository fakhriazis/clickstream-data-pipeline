
# Clickstream & Sales Analytics Data Pipeline

End-to-end data pipeline project to analyze website user behavior (clickstream) and sales performance, built using real-time and batch data processing tools. This project demonstrates how modern data stacks work together to deliver actionable insights for e-commerce or digital product businesses.

---

## Tujuan Proyek

Membangun sistem data pipeline untuk:

- Mengumpulkan data clickstream pengguna secara real-time dari situs web.
- Memuat data penjualan secara batch dari file CSV.
- Mengelola transformasi data menggunakan dbt.
- Mengatur orkestrasi job dengan Airflow.
- Menyediakan dashboard interaktif dengan Metabase.
- Mengotomatisasi eksekusi pipeline dengan CI/CD (GitHub Actions).

---

## Tech Stack

| Layer           | Tools/Frameworks                      |
|----------------|----------------------------------------|
| Ingestion       | Python Kafka Producer                 |
| Stream Platform | Apache Kafka                          |
| Raw Storage     | MinIO (S3-Compatible)                 |
| Database        | PostgreSQL                            |
| Transformation  | dbt (Data Build Tool)                 |
| Orchestration   | Apache Airflow                        |
| BI Dashboard    | Metabase                              |
| CI/CD           | GitHub Actions                        |

---

## Arsitektur Sistem

![Pipeline Diagram](./pipeline_diagram.png)

---

## 📁 Struktur Proyek

```
clickstream-data-pipeline/
├── airflow/                  # DAGs untuk pengolahan batch
├── clickstream_producer/    # Kafka producer untuk data clickstream
├── dbt/                     # Transformasi dan model analitik
│   ├── dbt_project.yml
│   ├── models/
│   │   ├── staging/
│   │   └── marts/
│   └── snapshots/
├── metabase/                # Pengaturan dashboard Metabase (opsional)
├── profiles.yml             # Konfigurasi koneksi dbt
├── pipeline_diagram.png     # Diagram visual pipeline
└── .github/workflows/
    └── dbt-ci.yml           # File CI/CD GitHub Actions
```

---

## ⚙️ Langkah Eksekusi

### 1. Clone Repository

```bash
git clone https://github.com/fakhribashiri/clickstream-data-pipeline.git
cd clickstream-data-pipeline
```

### 2. Jalankan Layanan (Opsional)

Jika menggunakan Docker Compose (belum tersedia di repo), pastikan Kafka, PostgreSQL, MinIO, dan Airflow sudah berjalan.

### 3. Jalankan Kafka Clickstream Producer

```bash
cd clickstream_producer
python producer.py
```

### 4. Jalankan dbt

```bash
cd dbt
dbt run --profiles-dir . --project-dir .
dbt test --profiles-dir . --project-dir .
```

### 5. Akses Dashboard Metabase

- Login ke Metabase
- Hubungkan ke database PostgreSQL
- Buat dashboard dari data marts hasil transformasi dbt

---

## ✅ Fitur yang Sudah Diimplementasikan

- [x] Simulasi real-time user clickstream via Kafka
- [x] Loader CSV sales ke PostgreSQL
- [x] Transformasi staging & marts dengan dbt
- [x] CI/CD dengan GitHub Actions untuk dbt
- [x] Dashboard Metabase (contoh: top product, conversion rate)

---

## CI/CD dengan GitHub Actions

File `.github/workflows/dbt-ci.yml` akan:

- Menyediakan service PostgreSQL via Docker
- Menjalankan `dbt debug`, `dbt run`, dan `dbt test` setiap ada push ke `main`

### Contoh Output CI
✅ `dbt debug` sukses  
✅ `dbt run` sukses  
✅ `dbt test` sukses  

---

## Contoh Visualisasi (Metabase)

- Unique Visitors per Hari
- Click-to-Sale Conversion Rate
- Top Viewed Products
- Revenue Over Time
- Average Basket Size

---

## Author

**Fakhri Azis Basiri**  
 fakhriazisbasiri@gmail.com  
 [Portofolio Proyek](https://github.com/fakhribashiri)

---

## Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE)

---

## 💡 Rencana Pengembangan

- Integrasi data warehouse (BigQuery/Snowflake)
- Implementasi Spark streaming untuk clickstream
- Realtime dashboard menggunakan Superset
- Tambah monitoring DAG dengan Airflow + Slack notif
