def f(x):
    a=0
    for i in range(2,x):
        if x%i==0:
            a+=1
    if x==0 or x==1:
        return 1
    elif x==2:
        return 0
    elif a==0:
        return 0
    elif a!=0:
        return 1
lst=eval(input())
lst2=[]
for x in lst:
    b=f(x)
    if b==0:
        lst2.append(x)
print(lst2)
            
