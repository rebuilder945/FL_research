lst=list(map(str,input().split()))
lst1=list(map(int,input().split()))
a=lst[lst1[0]]
b=lst[lst1[1]]
lst[lst1[0]]=b
lst[lst1[1]]=a
print(lst)
