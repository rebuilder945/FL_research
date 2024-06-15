a=eval(input())
avg=sum(a)/len(a)
m=sum(a)%len(a)
if m==0:
	print(int(avg))
elif isinstance(avg,float)==True:
	print("%.2f"%(avg))

