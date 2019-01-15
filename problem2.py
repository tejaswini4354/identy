import sys
import numpy as np 
high = sys.maxsize
arr = np.random.randint(high,size = (5,4))
print(arr)
for i in range(5):
	for j in range(4):
		if arr[i][j]>50:
			arr[i][j]  =100
print(arr)