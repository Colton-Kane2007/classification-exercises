from pydataset import data
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from acquire import get_telco_data, train_val_test
from sklearn.model_selection import train_test_split
from sklearn.metrics import \
accuracy_score,\
recall_score,\
precision_score,\
confusion_matrix,\
classification_report
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
import seaborn as sns
from sklearn.tree import\
DecisionTreeClassifier as DT,\
plot_tree,\
export_text
def prep_telco(df):
    ''' prep telco encodes all of the categorical columns from the telco dataset and changes strings into numbers for testing
    return: a pandas dataframe'''
    df['gender_encoded'] = df.gender.map({'Female': 1, 'Male': 0})
    df['partner_encoded'] = df.partner.map({'Yes': 1, 'No': 0})
    df['dependents_encoded'] = df.dependents.map({'Yes': 1, 'No': 0})
    df['phone_service_encoded'] = df.phone_service.map({'Yes': 1, 'No': 0})
    df['paperless_billing_encoded'] = df.paperless_billing.map({'Yes': 1, 'No': 0})
    df['churn_encoded'] = df.churn.map({'Yes': 1, 'No': 0})
    return df

    
    
    
    #dummy_df = pd.get_dummies(data=df[['gender', 'partner', 'dependents', 'phone_service', 'multiple_lines', 'online_security', 'online_backup', 'tech_support', 'streaming_tv', 'streaming_movies', 'paperless_billing', 'device_protection']], drop_first=True)
    #df = pd.concat([df, dummy_df], axis=1)
    #return df
