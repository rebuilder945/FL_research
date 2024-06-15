lst=eval(input())
a=0
for i in lst:
    a=a+i
l=len(lst)
if a%l==0:
    print(a//l)
elif a%l!=0:
    b=a/l
    print("%.2f"%b)

