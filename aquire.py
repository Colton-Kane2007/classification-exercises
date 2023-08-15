from env import user, host, password
import pandas as pd
import numpy as np
from pydataset import data
import os
# Make a function named get_titanic_data that returns the titanic data from the codeup data science database as a pandas data frame. 
# Obtain your data from the Codeup Data Science Database.

def get_titanic_data(
    db,
    user=user,
    password=password,
    host=host):
    '''
    grab data will query data from a specified positional argument (string literal)
    schema from an assumed user, password, and host provided
    that they were imported from an env
    
    return: a pandas dataframe
    '''
    query = '''SELECT * FROM passengers'''
    connection = f"mysql+pymysql://{user}:{password}@{host}/{db}"
    df = pd.read_sql(query, connection)
    return df
get_titanic_data('titanic_db')