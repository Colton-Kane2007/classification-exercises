from env import user, host, password
import pandas as pd
import numpy as np
from pydataset import data
import os
from sklearn.model_selection import train_test_split

def get_titanic_data(
    db,
    user=user,
    password=password,
    host=host):
    '''
    get titanic data will query data from a specified positional argument (string literal)
    schema from an assumed user, password, and host provided
    that they were imported from an env
    
    return: a pandas dataframe
    '''
    query = '''SELECT * FROM passengers'''
    connection = f"mysql+pymysql://{user}:{password}@{host}/{db}"
    df = pd.read_sql(query, connection)
    return df
get_titanic_data('titanic_db')
def train_val_test(df, strat, seed = 123):
    '''splits a pandas dataframe into 3 sample sets in order to test machine learning algorithms
    return: 3 pandas dataframes'''
    train, val_test = train_test_split(df, train_size = 0.8, random_state = seed, stratify = df[strat])
    val, test = train_test_split(val_test, train_size = 0.5, random_state = seed, stratify = val_test[strat])
    return train, val, test
def get_telco_data(
    db,
    user=user,
    password=password,
    host=host):
    '''
    get telco data will query data from a specified positional argument (string literal)
    schema from an assumed user, password, and host provided
    that they were imported from an env
    
    return: a pandas dataframe
    '''
    query = '''SELECT * FROM customers
                        LEFT JOIN contract_types
                        USING(contract_type_id)
                        LEFT JOIN internet_service_types
                        USING(internet_service_type_id)
                        LEFT JOIN payment_types 
                        USING(payment_type_id)'''
    connection = f"mysql+pymysql://{user}:{password}@{host}/{db}"
    df = pd.read_sql(query, connection)
    return df