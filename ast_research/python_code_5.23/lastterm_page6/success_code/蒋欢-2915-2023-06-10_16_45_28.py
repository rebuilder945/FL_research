#判断并输出水仙花数
sums=[]
def shuixian(n):
    m=n
    sum=0
    while n!=0:
        sum+=(n%10)**3
        n=n//10
    if sum==m:
        sums.append(m)
        print(m)
    else:
        return
l=eval(input())
for x in range(100,l+1):
    shuixian(x)
if len(sums)==0:
    print('none')

