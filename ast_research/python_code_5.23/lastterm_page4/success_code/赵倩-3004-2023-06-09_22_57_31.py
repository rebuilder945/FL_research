def s(x):
    for i in range(2,x):
        if x%i==0:
            return 0
    return 1
    if x==2:
        return 1
    elif x==1 or x==0:
        return 0
a=eval(input())
l=[]
for y in a:
    if s(y)==1:
        l.append(y)
print(l)






        







