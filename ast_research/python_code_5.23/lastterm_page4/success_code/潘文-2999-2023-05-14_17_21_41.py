lst=input().split()
n,m=input().split()
n,m=int(n),int(m)
if -len(lst)<=len(lst)and-len(lst)<=m<len(lst):
    lst[n],lst[m]=lst[m],lst[n]
    print(lst)
else:
    print("error")
