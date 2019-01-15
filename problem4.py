import sys
import numpy as np 
high = sys.maxsize
arr = np.random.randint(high,size = 10)
for i in range(10):
	if i%2!=0:
		arr[i][j]  = -10
