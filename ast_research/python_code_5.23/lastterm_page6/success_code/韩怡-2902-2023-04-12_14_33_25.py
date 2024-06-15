n=eval(input())
a=0
b=[1,1]
c=[0,1]
for i in range(1,n+1):
    son=b[-1]+b[-2]
    b.append(son)
    mother=c[-1]+c[-2]
    c.append(mother)
    a += son/mother
print("%.4f"%a)
