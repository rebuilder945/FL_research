def f(n):
    if n<=1:
        return False
    if n==2:
        return True
    for i in range(2,n):
        if n%i==0:
            return False
    return True
nums=eval(input())
ls=[]
for i in nums:
    if f(i):
        ls.append(i)
print(ls)
