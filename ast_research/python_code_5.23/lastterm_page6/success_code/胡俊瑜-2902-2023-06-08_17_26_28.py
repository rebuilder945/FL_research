nums=[]
n=int(input())
def fac(x):
	if x<=2:
		return 1
	a,b=1,1
	for x in range(3,x+1):
		v=a+b
		a,b=b,v
	return v
i=0
while i<n:
	i+=1
	nums.append(fac(i+2)/fac(i+1))
print("%.4f"% sum(nums))

