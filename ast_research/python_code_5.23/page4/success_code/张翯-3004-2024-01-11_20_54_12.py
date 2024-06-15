ls=eval(input())
lst=[]
a=0
for x in ls:
    for i in range(2,x):
        if x%i==0:
            a=1
    if a!=1:
        lst.append(x)
    else:
        a=0
print(lst)
