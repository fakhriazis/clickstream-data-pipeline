from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2025, 7, 16),
    'retries': 1
}

with DAG("sales_batch_etl", schedule_interval="@daily", default_args=default_args, catchup=False) as dag:

    task1 = BashOperator(
        task_id="load_from_minio",
        bash_command="python3 /opt/airflow/scripts/load_from_minio.py"
    )

    task2 = BashOperator(
        task_id="load_to_postgres",
        bash_command="python3 /opt/airflow/scripts/load_to_postgres.py"
    )

    task1 >> task2
