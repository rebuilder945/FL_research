lst=input().split()
lst2=lst[1:]
lst2 = list(map(int,lst2))
avg=sum(lst2)/len(lst2)
lst2.sorted(reversed=True)
print(lst[0],"%.2f %.2f %.2f %.2f"%(lst2[0],lst[1],lst[2],avg))
