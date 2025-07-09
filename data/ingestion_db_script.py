# THIS SCRIPT IS CONTRIBUTED BY RAKSHIT PANDEY

import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

logging.basicConfig(
    filename="logs/ingestion_db.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

engine=create_engine('sqlite:///inventory.db')

def ingest_db(df, table_name, engine):
    ''' function for continuous ingestion of dataframe into database tables as per industy practice '''
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
    

def load_raw_data():
    ''' This function will load the csv's as dataframes and ingest them in the db '''
    start=time.time()
    for file in os.listdir('C:\\Users\\raksh\\Desktop\\Data Analytics\\PYTHON_PROJECT_SALES_ANALYSIS\\data'):
        if '.csv' in file:
            df=pd.read_csv('C:\\Users\\raksh\\Desktop\\Data Analytics\\PYTHON_PROJECT_SALES_ANALYSIS\\data\\'+file)
            logging.info(f'Ingesting {file} in db')
            ingest_db(df, file[:-4], engine) 
    end=time.time()
    total_time=(end-start)/60
    logging.info('***************Ingestion Completed****************')
    logging.info(f'Total time taken: {total_time} minutes')


if __name__=='__main__':
    load_raw_data()