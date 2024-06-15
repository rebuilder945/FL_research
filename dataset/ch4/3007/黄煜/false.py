lst=eval(input())
n,m=map(int,input().split(","))
if n<=len(lst):
    for i in range(n,m):
        a=lst.pop(i)
        print(lst)
else:
    print("error")
