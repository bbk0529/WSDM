#Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from datetime import datetime
from dateutil.parser import parse


parse_dates = ['registration_init_time']
df = pd.read_csv('df.csv', index_col='msno', parse_dates=parse_dates)



df.groupby('n_tran').is_churn.mean().plot(kind='bar')
df.groupby('registered_via').is_churn.mean().plot(kind='bar')
df.groupby('gender').is_churn.mean().plot(kind='bar')
df.groupby('city').is_churn.mean().plot(kind='bar')
df.groupby('bins').is_churn.mean().plot(kind='bar')
  
df.registration_init_time.value_counts()
df.registration_init_time.value_counts().plot()







df.registration_init_time.value_counts().plot()



