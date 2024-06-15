a=eval(input())
avg=sum(a)/len(a)
if type(avg)==int:
    print(avg)
else:
    print("%.2f" %(avg))
