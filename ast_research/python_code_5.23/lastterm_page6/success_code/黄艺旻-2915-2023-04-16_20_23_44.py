def shui(n):
    if n in range(100,1000):
        a=n%10
        b=(n%100)-a
        c=(n-a-b*10)/100
        if a**3+b**3+c**3==n:
            return True
        else:
            return False
    else:
        return False
n=eval(input())
for i in range(n):
    if shui(i):
        print(i)
else:
    print('none')

