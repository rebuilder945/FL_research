lst=input()
n,m=input().split()
n=int(n)
m=int(m)
if n<len(lst) and m<len(lst):
    lst[n],lst[m]=lst[m],lst[n]
    print(lst)
else:
    print("error")
