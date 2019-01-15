import cv2


e = cv2.imread('Data for Question6.JPEG')


infile = r"Use it for question1.txt"
X=[]
with open(infile) as f:
    f = f.readlines()
for line in f:
	a = list(map(int,line.split()))
	x,x1,y,y1 = a[0],a[1],a[2],a[3]
	crop_img = e[y:y1, x:x1]
	X.append(crop_img) 

print(X)