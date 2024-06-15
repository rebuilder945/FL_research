l1=eval(input())
n,m=list(map(int,input().split(",")))
if m>len(l1) or n>len(l1) or n>m:
    print("error")
else:
    del l1[n:m:1]
    print(l1)
