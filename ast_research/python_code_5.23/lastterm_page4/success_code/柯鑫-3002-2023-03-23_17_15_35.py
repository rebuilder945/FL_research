list1=eval(input())
a=sum(list1)
b=len(list1)
c=a/b
d=int(c)
e=c-d
if e==0:
    print(d)
else:
    print("%.2f"%(c))
