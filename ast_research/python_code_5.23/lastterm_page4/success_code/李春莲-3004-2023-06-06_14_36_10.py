def f(x):
    for i in range(2,x):
        if x%i!=0:
            return True
l=eval(input())
l2=[]
for i in l:
    if f(i)==True:
        l2.append(i)
print(l2)
