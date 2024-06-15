def f(a):
    b=a
    c=0
    while a!=0:
        c+=(a%10)**3
        a=a//10
    if b==c:
        print(a)
        return True
flag=0
a=int(input())
for x in range(2,a+1):
    if f(x):
        flag = 1
if flag==0:
    print('none')
