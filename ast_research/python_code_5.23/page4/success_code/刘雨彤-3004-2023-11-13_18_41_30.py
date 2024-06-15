def isprime(n):
    if n<=1:
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                return False
    return True

num=eval(input())
res=[]
for n in num:
    if isprime(n):
        res.append(n)
print(res)


    
