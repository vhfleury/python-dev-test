from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import random, time, sqlite3, os
from sqlite3 import Error
from airflow import DAG
import pandas as pd
import os

def verifica_arquivo():
    """verifica se o DataFrame adult esta vazio, se sim, exclui"""
    
    path = "/home/churebas/projetos/python-dev-test/data/"
    
    arquivo = path + "adult.csv"
    
    if os.path.isfile(arquivo):
        df = pd.read_csv(arquivo)

        if df.shape[0] == 0:    
            os.remove(arquivo)
            parar = True
        else:
            parar = False
    else:
        parar = True

    if parar:
        os.system("export AIRFLOW_HOME=$(pwd)/airflow")
        os.system("airflow dags pause popula_bd")
        print("parou")

def percorre_df(quantidade):
    """puxa os dados do dataframe adult e popula banco de dados """

    path = "/home/churebas/projetos/python-dev-test/data/"
    
    arquivo = path + "adult.csv"
    df = pd.read_csv(arquivo)

    if quantidade > df.shape[0]:
        quantidade = df.shape[0]

    usar = df.iloc[:quantidade]
    
    coon = sqlite3.connect(path + "adult.db")
    usar.to_sql("adult", coon, index=False, if_exists="append")

    
    df.drop(index=[n for n in range(quantidade)], inplace=True)
    df.to_csv(arquivo, index=False)
        
default_args = {
    'owner': 'victor hugo',
    "email": ['vh15fleury@hotmail.com'],
    'retries': 1,
    }

with DAG(
    
    'popula_bd',
    default_args=default_args,
    start_date = datetime.now(),
    schedule_interval = timedelta(seconds=10),
    catchup=False,
    tags=['ETL']
    
    ) as dag:
        t1 = PythonOperator(
        task_id='verifica_arquivo',
        python_callable=verifica_arquivo)

        t2 = PythonOperator(
        task_id='popula_adult',
        python_callable=percorre_df,
        op_kwargs={'quantidade': 1630}),
        
        t1 >> t2