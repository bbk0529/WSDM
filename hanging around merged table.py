#진희님이 merged 시킨 전체 테이블을 대상으로 그래프 


#Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from datetime import datetime
from dateutil.parser import parse

#%matplotlib inline
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

parse_dates = ['transaction_date', 'membership_expire_date','registration_init_time']


memNall_data = 'memNall.csv'
memNall = pd.read_csv('memNall.csv', index_col='msno', parse_dates=parse_dates)

bins = [0,18,25,35,60,100]

cutData=pd.cut(memNall.bd, bins)
memNall['bins']=cutData


count=memNall.index.value_counts()




In [42]: count.size
Out[42]: 961431

In [43]: memNall.index.nunique()
Out[43]: 961431


count[:10]

memNall[memNall.index=='72gJqt1O31E/WoxAEYFn9LHNI6mAZFGera5Q6gvsFkA=']

for i in count[:10].index :
	memNall[memNall.index==i].describe()



##GRAPH
memNall.groupby('bins').is_churn.mean().plot(kind='bar')
memNall.groupby('is_auto_renew').is_churn.mean().plot(kind='bar')
memNall.groupby('payment_method_id').is_churn.mean().plot(kind='bar')
memNall.groupby('payment_plan_days').is_churn.mean().plot(kind='bar')
memNall.groupby('plan_list_price').is_churn.mean().plot(kind='bar')


#GROUP BY 
memNall.groupby('bins').is_churn.mean()
memNall.groupby('is_auto_renew').is_churn.mean()
memNall.groupby('payment_method_id').is_churn.mean()
memNall.groupby('payment_plan_days').is_churn.mean()
memNall.groupby('plan_list_price').is_churn.mean()


