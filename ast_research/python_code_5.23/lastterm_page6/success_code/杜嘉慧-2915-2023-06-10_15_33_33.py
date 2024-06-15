def flowernumber(n):
    sums=0
    while n!=0:
        n=n%10
        sums+=n**3
    if n==sums:
        return n
n=int(input())
flag=False
for x in range(2,n):
    if flowernumber(x)==x:
        print(x)
        flag=True
if flag==False:
    print("none")

