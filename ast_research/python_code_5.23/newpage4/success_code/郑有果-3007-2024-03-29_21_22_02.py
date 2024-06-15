lst=eval(input())
a,b=eval(input())
n=min(a,b)
m=max(a,b)
if m<len(lst):
    for i in range(n,m):
        del lst[i]
    print(lst)
else:
    print("error")


