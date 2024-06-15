ls1=eval(input())
ls2=[]
for x in ls1:
	k=0
	for i in range(1,x+1):
		if x%i==0:
			k+=1
	if k==2:
		ls2.append(x)
print(ls2)
	

