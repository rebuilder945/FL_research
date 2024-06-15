lst=eval(input())
n=len(lst)
sum=0
for i in lst:
    sum+=i
x=sum/n
if type(x)==int:
    x=int(x)
    print("%d"%x)
else:
    print("%.2f"%x)
