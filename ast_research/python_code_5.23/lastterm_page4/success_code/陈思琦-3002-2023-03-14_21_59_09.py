a=eval(input())
avg=eval(sum(a)/len(a))
if type(avg)==int:
    print(avg)
else:
    print("%.2f" %(avg))
