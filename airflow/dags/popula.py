from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import pandas as pd
import random, time
import pandas as pd
from sqlite3 import Error
import sqlite3

def percorre_df(quantidade):
    
    path = "/home/churebas/projetos/python-dev-test/data/"
    
    arquivo = path + "adult.csv"
    df = pd.read_csv(arquivo)

    if quantidade > df.shape[0]:
        quantidade = df.shape[0]

    usar = df.iloc[:quantidade]
    
    coon = sqlite3.connect(path + "teste.db")
    usar.to_sql("adult", coon, index=False, if_exists="append")

    
    df.drop(index=[n for n in range(quantidade)], inplace=True)
    df.to_csv(arquivo, index=False)
        
        
default_args = {
    'owner': 'victor hugo',
    "email": ['vh15fleury@hotmail.com'],
    "start_date" : datetime.now(),
    # "schedule_interval": datetime(seconds=10)

}

with DAG(
    'popula_bd',
    default_args=default_args,
    start_date = datetime.now(),
    schedule_interval = timedelta(seconds=10),
    # schedule_interval = None,
    catchup=False,
    tags=['teste']
    
    ) as dag:
        t3 = PythonOperator(
        task_id='popula_adult',
        python_callable=percorre_df,
        op_kwargs={'quantidade': 1630})
        