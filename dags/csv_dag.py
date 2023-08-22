from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime,timedelta
from airflow.utils.dates import days_ago
from main import download_csv_from_link, count_rows_in_csv, delete_csv_file


csv_url = "https://www.stats.govt.nz/assets/Uploads/Annual-enterprise-survey/Annual-enterprise-survey-2021-financial-year-provisional/Download-data/annual-enterprise-survey-2021-financial-year-provisional-csv.csv"
file_name = "downloaded.csv"

# initializing the default arguments that we'll pass to our DAG
default_args = {
    'owner': 'airflow',
    'start_date': days_ago(5),
    'email': ['airflow@my_first_dag.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}
csv_dag = DAG(
    'csv_dag',
    default_args=default_args,
    description='csv_dag',
    schedule_interval=timedelta(days=1),
)

task1= PythonOperator(
    task_id="downlaoding_csv",
    dag=csv_dag,
    python_callable=download_csv_from_link,
    op_kwargs={
    "url": csv_url,
    'save_path':file_name
}

)
task2= PythonOperator(
    task_id="counting_rows",
    dag=csv_dag,
    python_callable=count_rows_in_csv,
    op_kwargs={
    "csv_path": file_name
}
)
task3 = PythonOperator(
    task_id="deleting_rows",
    dag=csv_dag,
    python_callable=delete_csv_file,
    op_kwargs={
    'file_path': file_name
    
    }
)


task1>> task2 >> task3
