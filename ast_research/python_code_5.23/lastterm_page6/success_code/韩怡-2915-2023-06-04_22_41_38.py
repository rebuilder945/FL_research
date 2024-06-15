def shuishu(n):
    a = n % 10
    b = n // 10 % 10
    c = n // 100
    if n == a**3+b**3+c**3:
        return True
    else:
        return False

n = eval(input())
if 100 <= n <=999:
    ls=[]
    for i in range(100,n+1):
        if shuishu(i):
            ls.append(i)
            print(i)
        else:
            pass
    if ls==[]:
        print("none")
else:
    print("none")

