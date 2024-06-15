flag=0
n=int(input())
for x in range(100,n+1):
    if (x%10)**3+(x//10%10)**3+(x%100)**3==x:
        print(x)
        flag=1
if flag==0:
    print("none")
