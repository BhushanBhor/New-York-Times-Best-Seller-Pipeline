import json
import airflow
import requests
import smtplib
import pandas as pd
from airflow import DAG
from datetime import datetime
from datetime import timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from airflow.operators.bash_operator import BashOperator
from airflow.operators.email_operator import EmailOperator
from airflow.operators.python_operator import PythonOperator

default_args = {
    'owner': 'airflow',    
    'start_date': airflow.utils.dates.days_ago(6),
    # 'end_date': datetime(2018, 12, 30),
    'depends_on_past': False,
    'email': ['bhushan.pop@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'schedule_interval': '@weekly',
}

dag = DAG(
    dag_id = 'NYTimes',
    default_args=default_args,
    description='New York Times Best Seller DAG',
    # Continue to run DAG once per Week
    schedule_interval=timedelta(days=1),
)

#Acquire Data from NYTimes API
t1 = BashOperator(task_id='data_acquisition',
                    #python_callable=get_list,
                    bash_command = 'python /home/user/t1.py ',
                    #provide_context=True,
                    #poke_interval=5,
                    dag=dag)

#Emailing the Users to 
t1 = BashOperator(task_id='data_acquisition',
                    #python_callable=get_list,
                    bash_command = 'python /home/user/t2.py',
                    #provide_context=True,
                    #poke_interval=5,
                    dag=dag)

t2 = EmailOperator(
        task_id='emailing_recepients',
        to='bhushan@gmail.com',
        subject='Airflow Alert',
        html_content="Please find the attachment of NewYork Times Best Sellers",
        files=['combined'],
        dag=dag
)

t1 >> t2
