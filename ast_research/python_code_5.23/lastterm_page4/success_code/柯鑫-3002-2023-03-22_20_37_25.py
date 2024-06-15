list=input()
a=sum(list)/len(list)
b=a-int(a)
if b==0:
    print(int(b))
elif b!=0:
    print("%.2f"%b)
