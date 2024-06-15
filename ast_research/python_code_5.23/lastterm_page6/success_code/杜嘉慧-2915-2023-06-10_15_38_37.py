def flowernumber(n):
    sums=0
    a=n
    while n!=0:
        sums+=(n%10)**3
        n=n//10
    if a==sums:
        print(n)
        return True
n=int(input())
flag=False
for x in range(2,n+1):
    if flowernumber(x):
        flag=True
if flag==False:
    print("none")

