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

#End of time
print(round((time.time()-start)/3600))

#creating AVG table
avg={}
for row in result :
	avg[row.index] = result[row.index] / count[row.index]

#####################################################
#converted it as DataFrame in Pandas
df=pd.DataFrame(avg, index=header[2:]).transpose()
#save as csv format
df.to_csv('avg_of_user_logs.csv')



##########TO READ CSV FILE
import numpy as np
import pandas as pd

df=pd.read_csv('sums_of_user_logs.csv',  index_col=0)
