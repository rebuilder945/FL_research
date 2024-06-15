
n=int(input())
lst=[i+1 for i in range(n)]
lst2=[]
for i in range(len(lst)):
    if i!=0:
        lst2.append(lst[i])
lst2.append(lst[0])
print(lst2)
