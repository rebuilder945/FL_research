name,*grade=input().split()
lst=list(map(int,grade))
avg=sum(lst)/3
lst.sort(reverse=True)
print("%s"%name,end=" ")
for x in lst:
    print("%.2f"%x,end=" ")
print("%.2f"%avg)
