import numpy as np
import pandas as pd
import time

file=open('user_logs.csv','r')
header=file.readline().split(',')
size=len(header)
result={}

i=0
start=time.time()
chunk=1000000
while(1):
	for _ in range(chunk) : 
		line=file.readline()
		if not line: break #meeting EOF, the loop ends. 
		row=line.split(',')
		index=row[0] + row[1][:4]
		data = np.array(row[2:], dtype='float').astype('int')
		result[index]= result.get(index, np.zeros(size-2, dtype='int')) + data
		
	#checking progress
	i+=1
	print('Read rows : ' + str(i*chunk) + '\tSize of dictionary : ' +str((len(result))) + '\t' + str(round(time.time() - start)) + ' secs')

#End of time
print(round((time.time()-start)/3600))



#####################################################


#converted it as DataFrame in Pandas
df=pd.DataFrame(result, index=header[2:]).transpose()


#save as csv format
df.to_csv('sums_of_user_logs.csv')



##########TO READ CSV FILE
import numpy as np
import pandas as pd

df=pd.read_csv('sums_of_user_logs.csv',  index_col=0)
