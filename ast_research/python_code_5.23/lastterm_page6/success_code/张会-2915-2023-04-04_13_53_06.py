def shuixian(n):
    a = n%10
    b =n//10%10
    c =n//100
    if a**3 + b**3 + c**3 ==n:
        return True
    else:
        return False
                
n = eval(input())
flag = 0
for i in range(100,n+1):
    if shuixian(i):
        if 99<i<1000:
            print(i)
            flag = 1
if flag == 0:
    print("none")

