list=eval(input())
t=0
for i in list:
    t=t+i
l=len(list)
a=t/l
if a%1==0:
    print("%d"%a)
else:
    print("%.2f"%a)
