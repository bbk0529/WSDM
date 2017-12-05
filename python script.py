#Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from datetime import datetime
from dateutil.parser import parse

#%matplotlib inline

#from IPython.core.interactiveshell import InteractiveShell
#InteractiveShell.ast_node_interactivity = "all"

parse_dates = ['transaction_date', 'membership_expire_date','registration_init_time']
memNall_data = 'memNall.csv'

#memNall = pd.read_csv(memNall_data, nrows=100, index_col='msno', parse_dates=parse_dates
memNall = pd.read_csv('memNall.csv', index_col='msno', parse_dates=parse_dates)

bins = [0,18,25,35,60,100]

cutData=pd.cut(memNall.bd, bins)
memNall['bins']=cutData


#각 회원별 transaction 숫자 count
count=pd.value_counts(memNall.index)

memNall[pd.value_counts(memNall.index) >50]

bins2=[]
for i in range(26) : bins2.append(i*10)

count=pd.value_counts(memNall.index)  
pd.cut(count, bins2) 

##GRAPH
#grouped by age-group,
memNall.groupby('bins').is_churn.mean().plot(kind='bar')


memNall.groupby('is_auto_renew').is_churn.mean()
memNall.groupby('is_auto_renew').is_churn.mean().plot(kind='bar')

memNall.groupby('payment_method_id').is_churn.mean()
memNall.groupby('payment_method_id').is_churn.mean().plot(kind='bar')


memNall.groupby('payment_plan_days').is_churn.mean()
memNall.groupby('payment_plan_days').is_churn.mean().plot(kind='bar')



memNall.groupby('plan_list_price').is_churn.mean()
memNall.groupby('plan_list_price').is_churn.mean().plot(kind='bar')



In [70]: mem_over_60_transaction=memNall[pd.value_counts(memNall.index)>60]




