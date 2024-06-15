lst=eval(input())
n,m=map(int,input().split(','))
if n<=len(lst):
    for x in range(n,m):
        lst.pop(x)
    print(lst)
else:
    print("error")

