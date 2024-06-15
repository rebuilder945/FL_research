list=eval(input())
a=sum(list)%len(list)
b=sum(list)/len(list)
if a==0:
    print("%d"%b)
else:
    print("%.2f"%b)

