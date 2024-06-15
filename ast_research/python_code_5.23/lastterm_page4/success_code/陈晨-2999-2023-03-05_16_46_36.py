lst=list(input().split())
num=list(input().split())
for x in range(0,len(num)):
    num[x]=int(num[x])
a,b=num[0],num[1]
ls=lst[a]
lst[a]=lst[b]
lst[b]=ls
print(lst)
