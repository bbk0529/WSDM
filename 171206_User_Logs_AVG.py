import numpy as np
import pandas as pd
import time

file=open('user_logs.csv','r')
header=file.readline().split(',')
size=len(header)
result={}
count={}

i=0
start=time.time()
chunk=1000000

while(1) :
	for _ in range(chunk) : 
		line=file.readline()
		row=line.replace('\n','').split(',')
		index=row[0]
		data=row[2:]
		data= np.array(data, dtype='float').astype('int')
		result[index]= result.get(index, np.zeros(size-2, dtype='int')) + data
		count[index]= count.get(index, 0)+1
	i+=1
	print('Rows : ' + str(i*chunk) 
		+ '\tResult : ' +str((len(result))) 
		+ '\tCount : ' + str(len(count))
		+ '\tTime : ' + str(round(time.time() - start)) + ' s'
	)


###########READ 2nd file to merge ###################

file=open('user_logs_v2.csv','r')
line=file.readline()
while(1) :
	for _ in range(chunk) : 
		line=file.readline()
		row=line.replace('\n','').split(',')
		index=row[0]
		data=row[2:]
		data= np.array(data, dtype='float').astype('int')
		result[index]= result.get(index, np.zeros(size-2, dtype='int')) + data
		count[index]= count.get(index, 0)+1
	i+=1
	print('Rows : ' + str(i*chunk) 
		+ '\tResult : ' +str((len(result))) 
		+ '\tCount : ' + str(len(count))
		+ '\tTime : ' + str(round(time.time() - start)) + ' s'
	)

###############creating AVG table####################
avg={}
for row in result.keys() :
	avg[row] = result[row] / count[row]

#####################################################
#converted it as DataFrame in Pandas
#save as csv format

df_avg=pd.DataFrame(avg, index=header[2:]).transpose()
df_avg.to_csv('avg_of_user_logs_171205.csv')


df_sum=pd.DataFrame(result, index=header[2:]).transpose()
df_sum.to_csv('sum_of_user_logs_171205.csv')

df_count=pd.DataFrame(count, index=['count']).transpose()
df_count.to_csv('count_of_user_logs_171205.csv')


###########TO READ CSV FILE###########################
import numpy as np
import pandas as pd

df_avg=pd.read_csv('avg_of_user_logs_171205.csv',  index_col=0)
df_sum=pd.read_csv('sum_of_user_logs_171205.csv',  index_col=0)
df_count=pd.read_csv('count_of_user_logs_171205.csv',  index_col=0)



