lst=eval(input())
a=len(lst)
b=sum(lst)/a
c=sum(lst)//a
if b-c==0:
    print(c)
else:
    print ("%.2f"%b)

