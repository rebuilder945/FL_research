list=eval(input())
a=[]
for x in list:
    if x == 1:
        continue
    elif x==2:
        a.append(x)
    else:
        for i in range(2,x):
            if x%i==0:
                break
            if i==x-1:
                a.append(x)
print(a)
