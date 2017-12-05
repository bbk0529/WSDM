# transaction count를 활용해서 membershpi date transaction date형태를 확인하는 것. 

#Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from datetime import datetime
from dateutil.parser import parse

#%matplotlib inline

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"


parse_dates = ['transaction_date', 'membership_expire_date']
parse_dates2 = ['registration_init_time']

train_data = 'train.csv'
train_data_v2= 'train_v2.csv'
transaction_data = 'transactions.csv'
transaction_data_v2='transactions_v2.csv'
member_data = 'members_v2.csv'
transaction = pd.read_csv(transaction_data, index_col='msno', parse_dates=parse_dates)
transaction_v2 = pd.read_csv(transaction_data_v2, index_col='msno', parse_dates=parse_dates)



merged_transaction=pd.concat([transaction, transaction_v2])


count=merged_transaction.index.value_counts()
count100=count[:100]


for i in count100.index:
	merged_transaction[merged_transaction.index==i][['transaction_date', 'membership_expire_date']].describe()




