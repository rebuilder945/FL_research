lst=input().split(",")
n,m=eval(input())
if n<=len(lst):
    for i in range(m):
        lst.append(lst.pop(n-1))
else:
    print("error")
