#判断并输出水仙花数
sums=[]
def shuixian(n):
    sum=0
    while n!=0:
        sum+=(n%10)**3
        print(sum)
        n=n//10
    if sum==n:
        sums.append(n)
        print(n)
    else:
        return
l=eval(input())
for x in range(100,l+1):
    shuixian(x)
if len(sums)==0:
    print('none')

