def prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

ls=eval(input())
pr=[]
for i in ls:
    if i>=2:
        a=prime(i)
        if a==True:
            pr.append(i)
print(pr)
