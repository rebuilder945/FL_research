def s(x):
    for i in range(2,x):
        if x%i==0 and i!=0 and i!=1:
            return 0
        elif i==0 or i==1:
            return 0
    return 1
a=eval(input())
l=[]
for y in a:
    if s(y)==1:
        l.append(y)
print(l)






        







