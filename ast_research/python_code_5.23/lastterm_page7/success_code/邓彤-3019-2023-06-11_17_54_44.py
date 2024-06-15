lst=input().split(" ")
name=lst.pop(0)
lst=list(map(int,lst))
avg=sum(lst)/len(lst)
lst.sort(reverse=True)
print("%s %.2f %.2f %.2f %.2f"%(name,lst[0],lst[1],lst[2],avg))

