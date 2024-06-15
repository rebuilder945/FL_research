def shui(n):
    if n in range(100,1001):
        a=n%10
        b=((n%100)-a)/10
        c=(n-a-b*10)/100
        if a**3+b**3+c**3==n:
            return True
        else:
            return False
    else:
        return False
n=eval(input())
m=[]
if n not in range(100,1001):
    print('none')
else:
    for i in range(100,n+1):
        if shui(i):
            print(i)
            m.append(i)
    if m==[]:
        print('none')

