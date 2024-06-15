def f(n):
    a=n
    t=0
    while n!=0:
        t+=(n%10)**3
        n=n//10
    if a ==t:
        print(a)
        return True
flag=0
n=int(input())
for i in range (2,n+1):
    if f (i):
        flag=1
if flag ==0:
    print("none")
