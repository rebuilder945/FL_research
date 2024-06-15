def shuixianhua(n):
    n2=n
    pandaun=0
    while n2!=0:
        panduan+=(n2%10)**3
        n2=n2//10
    if panduan==n:
        print(n)
        return True
flag=0
nn=eval(input())
for i in range(nn+1):
    if shuixianhua(i):
        flag=1
if flag==0:
    print('none')
    


