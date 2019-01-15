infile = r"Data Question 6 Transaction.log"

with open(infile) as f:
    f = f.readlines()
sum = 0
for line in f:
	a = list(line.split())
	if a[0]=='D':
		sum = sum+int(a[1])
	elif a[0] == 'W':
		sum = sum-int(a[1])

fi = open("Data Question 6 Transaction.log", "a")
fi.write("Available Balance :"+str(sum)) 