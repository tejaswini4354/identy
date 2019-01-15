import numpy as np 
def func():
    high = 100
    n = np.random.randint(high)
    arr = np.random.randint(high,size = n)
    arr1 = np.random.choice(a=[False, True], size=n) 
    arr3=[]
    for i in range(n):
    	if arr1[i]:
    	    arr3.append(arr[i])
    return arr3
