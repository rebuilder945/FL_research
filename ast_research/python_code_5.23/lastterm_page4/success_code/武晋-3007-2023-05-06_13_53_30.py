lst=list(input())
n=input()
m=input()
n=int(n)
m=int(m)
if n<len(lst) or m<len(lst):
    if n<m:
        del lst[n,m]
    else:
        del lst[m+1,n+1]
else:
    print("error")
