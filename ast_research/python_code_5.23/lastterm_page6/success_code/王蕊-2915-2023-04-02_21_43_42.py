#水仙花数
def flower(n):
    a=n
    s=0
    while n!=0:
        s+=(n%10)**3
        n=n//10
    if a==s:
            print(a)
            return True

flag=0
n=int(input())
for i in range(2,n+1):
    if flower(i):
        flag=1
if flag==0:
    print("none")

