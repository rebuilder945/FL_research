lst=input().split()
name=lst[0]
english=int(lst[1])
python=int(lst[2])
math=int(lst[3])
lst2=lst[1:]
lst2=list(map(int,lst2))
lst2.sort(reverse=True)
avg=sum(lst2)/len(lst2)
print(name,end=" ")
for x in lst2:
    print("{:.2f}".format(x),end=" ")
print(avg)
