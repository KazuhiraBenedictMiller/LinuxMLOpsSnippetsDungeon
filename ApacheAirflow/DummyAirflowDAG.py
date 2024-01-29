from datetime import datetime, timedelta, timezone
import time

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

DAGTempFiles = "./"
        
def E():
    with open(DAGTempFiles + "newfile.txt", "w") as f:
        f.write("randomtext")

args = {
    'owner': 'admin',
    'retries': 2,
    'retry_delay': timedelta(minutes=5)
    }    

dag = DAG(
    'E',
    default_args = args,
    description = 'E',
    schedule_interval = '@hourly',
    start_date = datetime(2024, 1, 1),
    catchup=False
    )

EE = PythonOperator(
    task_id = 'Extract',
    python_callable = E,
    dag = dag,
)

EE
