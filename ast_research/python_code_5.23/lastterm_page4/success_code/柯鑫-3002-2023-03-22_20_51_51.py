list1=input()
a=sum(list1)/len(list1)
b=isinstance(a,int)
if b==True:
    print(int(a))
else:
    print("%.2f"%a)
