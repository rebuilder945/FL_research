a=eval(input())
avg=sum(a)/len(a)
if isinstance(avg,int)==True:
	print(int(avg))
else:
	print("%.2f"%(avg))

