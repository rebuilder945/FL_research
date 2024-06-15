list=input()
a=sum(list)/len(list)
b=isinstance(a,int)
if b==True:
    print(int(a))
else:
    print("%.2f"%a)
