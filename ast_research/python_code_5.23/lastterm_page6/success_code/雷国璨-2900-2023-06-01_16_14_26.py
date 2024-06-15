def isprime(num):
    if num==0 or num==1:
        return False
    for j in range(2,int(i**0.5)+1):
        if num%j==0:
            return False
    else:
        return True
n=eval(input())
if n>1 and type(n)==int:
    lst=[]
    for i in range (n):
        if isprime(i) and str(i)==str(i)[::-1]:
            lst.append(i)
    print(*lst)
else:
    print("illegal input")
