def shuixianhua(n):
    a=n%10
    m=n//10
    b=m%10
    c=n//100
    if n==a**3+b**3+c**3:
        return True
    return False

n=eval(input())
ls=[]
for i in range(n+1):
    if 99<i<1000 and shuixianhua(i):
        ls.append(i)
if ls==[]:
    print('none')
else:
    for x in ls:
        print(x)

