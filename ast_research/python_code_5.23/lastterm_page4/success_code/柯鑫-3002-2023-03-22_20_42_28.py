list=input()
a=sum(list)/len(list)
b=a-int(a)
if b==0:
    print(int(a))
else:
    print("%.2f"%a)
