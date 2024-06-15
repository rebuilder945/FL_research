def f(x):
    if x%2!=0:
        return x*3+1
    elif x%2==0:
        return x//2
a=eval(input())
lst1=[]
while a!=1:
    a=f(a)
    lst1.append(str(a))
print(",".join(lst1))




