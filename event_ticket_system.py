import mysql.connector
from sqlalchemy import create_engine
import pandas as pd
from datetime import date, datetime, timedelta


def load_third_party(engine, file_path_csv):
    
    df_tickets = pd.read_csv(file_path_csv, delimiter=',',
                             names=['ticket_id','trans_date', 'event_id', 'event_name',\
                                    'event_date', 'event_type', 'event_city','customer_id',\
                                        'price', 'num_tickets'])
    print(df_tickets.head())

    df_tickets.to_sql("third_party_sales",
          engine,
          if_exists="append",  index = False)
    
    return

engine = create_engine('mysql+mysqlconnector://username:password@hostname:port/db_name')
file_path_csv = '/Users/meetapandit/DE_Bootcamp/python_data_pipeline_miniproject/third_party_sales_1.csv'
load_third_party(engine, file_path_csv)
