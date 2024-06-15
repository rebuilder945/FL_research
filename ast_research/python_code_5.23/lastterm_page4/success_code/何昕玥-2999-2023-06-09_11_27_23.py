str=input().split(" ")
lst=list(str)
n,m=map(int(),input().split(" "))
n and m<len(lst)
lst[n],lst[m]=lst[m],lst[n]
print(lst)
