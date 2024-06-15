def s(x):
    for i in range(2,x):
        if x%i==0:
            return 0
    return 1
a=eval(input())
l=[]
for n in a:
    if n==1 or n==0:
        a.remove(n)
for y in a:
    if s(y)==1:
        l.append(y)
print(l)






        







