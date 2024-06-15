lst=eval(input())
n=len(lst)
sum=0
for i in lst:
    sum+=i
x=sum/n
if x==sum//n:
    print(int(x))
else:
    print("%.2f"%x)
