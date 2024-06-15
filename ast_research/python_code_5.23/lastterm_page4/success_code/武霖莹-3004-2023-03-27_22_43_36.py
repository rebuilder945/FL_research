def IsPrime(n):
    if n <2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
        if i*i>n:
            return True
    return True
lst=eval(input())
lstR=[x for x in lst if IsPrime(x)]
print(lstR)




