def flowernumber(n):
    sums=0
    while n!=0:
        sums+=(n%10)**3
        n=n//10
    if n==sums:
        return True
n=int(input())
flag=False
for x in range(2,n+1):
    if flowernumber(x):
        print(x)
        flag=True
if flag==False:
    print("none")

