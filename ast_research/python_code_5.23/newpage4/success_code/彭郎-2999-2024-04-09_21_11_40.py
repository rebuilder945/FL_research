def switch(lst,m,n):
    lst[m],lst[n]=lst[n],lst[m]
    return lst
lst=input().split()
n,m=input().split()
n,m=int(n),int(m)
if n<len(lst) and m <len(lst):
    a=switch(lst,m,n)
    print(a)
