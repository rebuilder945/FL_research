list1=eval(input())
a=sum(list1)
b=len(list1)
c=a%b
d=a/b
if c==0:
    print(int(d))
else:
   print("%.2f"%(d))


