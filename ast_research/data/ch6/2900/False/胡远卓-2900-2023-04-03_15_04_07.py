import math
def isprime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True
def isprd(x):
    return str(x)==str(x)[::-1]

x=eval(input())
if x<0 or type(x)==type(0.5):
    print("illegal input")
else:
    res=""
    for i in range(2,x+1):
        if isprime(i) and isprd(i):
            res=res+str(i)+' '
    print(res[:-1])
