def shuixianhua(x):
    a=x%10
    b=(x//10)%10
    c=((x//10)//10)%10
    if x==a**3+b**3+c**3:
        return True
    else:
        return False

n=eval(input())
m=0
for x in range(100,n):
    if shuixianhua(x):
        print(x)
        m+=1
if m==0:
    print('none')
