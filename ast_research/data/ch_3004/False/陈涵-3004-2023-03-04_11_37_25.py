def isprime(n):
    if n<=2:
        return True
    else:
        for x in range(2,n):
            if n%x==0:
                return False
            else:
                return True    
s = eval(input(""))
m =[n for n in s if isprime(n)==True]
print(m)                               

