def isprime(n):
    if n>1 and n<=2:
        return True
    elif n<=1:
        return False
    else:
        for x in range(2,n):
            if n%x==0:
                return False
    return True    
n=eval(input())
if n <=0 or type(n)==float:
    print("illegal input")
else:
    num=list(range(1,n+1))
    num2=[str(x) for x in num if isprime(x)==True]
    num3=[i for i in num2 if i[::-1]==i]
    print(" ".join(num3))

            
