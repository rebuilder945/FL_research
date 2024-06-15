a=eval(input())
avg=sum(a)/len(a)
if avg-int(avg)==0:
    print(int(avg))
else:
    print("%.2f" %(avg))
