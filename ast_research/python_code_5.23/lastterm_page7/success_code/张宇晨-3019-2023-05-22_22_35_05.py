lst1=["english","python","math"]
lst = list(input().split(" "))

lst2=[]
for i in range(1,len(lst)):
    lst2.append(float(lst[i]))
lst2.sort(reverse=True)
aver = sum(lst2)/3
lst2.append(f"{aver:.2f}")
lst2.insert(0,lst[0])
for x in range(1,4):
    lst2[x]=f"{lst2[x]:.2f}"
print(*lst2)
