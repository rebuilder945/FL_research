n=eval(input())
list1=[]
for i in range(n+1):
    a=i+2/i+1
    if i+1==0:
        continue
    else:
        list1.append(a)
a=sum(list1)
print("%.4f"%a)
