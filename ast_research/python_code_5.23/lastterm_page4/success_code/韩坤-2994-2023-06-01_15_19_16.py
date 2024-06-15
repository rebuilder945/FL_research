lst=list(map(int,input().split(",")))
n,m=map(int,input().split(","))
if n>len(lst)-1 or n<(-1)*len(lst):
    print("error")
else:
    lst1=[lst[n]]*m
    lst.extend(lst1)
    print(lst)
