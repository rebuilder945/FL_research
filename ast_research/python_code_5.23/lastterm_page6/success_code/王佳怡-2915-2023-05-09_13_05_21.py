def shui(x):
    a=x%100
    b=(x//10)%10
    c=x//100
    a**3+b**3+c**3==x
    print(x)
    return True
flag=0
n=eval(input())
for i in range(0,n+1):
    if shui(i):
        flag=1
    
if flge==0:
    print("none")
