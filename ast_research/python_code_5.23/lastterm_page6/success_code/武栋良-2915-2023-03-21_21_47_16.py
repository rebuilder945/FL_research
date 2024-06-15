def shuixianshu(n):
    a = n%10
    b = n//10%10
    c = n//100
    if a**3+b**3+c**3==n:
        return True
    else:
        return False
n = eval(input())
if n>=1000:
    for i in range(100,1000):
        if shuixianshu(i):
            print(str(i))
        else:
            print("error")
else:
    for i in range(100,n+1):
        if shuixianshu(i):
            print(str(i))
        else:
            print("error")

