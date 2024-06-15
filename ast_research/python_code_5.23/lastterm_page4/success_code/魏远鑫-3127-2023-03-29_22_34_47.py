list=eval(input())
a=sum(list)
b=len(list)
c=a/b
if c-int(c)>0:
    print("%.2f"%c)
if c-int(c)==0:
    print(int(c))
