from datetime import datetime, timedelta, timezone
import time

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.decorators import dag, task

'''
https://airflow.apache.org/docs/apache-airflow/stable/tutorial_taskflow_api.html
'''


DAGTempFiles = "/opt/airflow/dags/"
  
args = {
    'owner': 'admin',
    'retries': 2,
    'retry_delay': timedelta(minutes=5)
    }      
  
@dag(default_args = args,
    description = 'E',
    schedule_interval = '@hourly',
    start_date = datetime(2024, 1, 1),
    catchup=False)
def maindag():
    @task()  
    def E():
        with open(DAGTempFiles + "marameo.txt", "w") as f:
            f.write("miao")

    E()

# Export the DAG object
maindag = maindag()
