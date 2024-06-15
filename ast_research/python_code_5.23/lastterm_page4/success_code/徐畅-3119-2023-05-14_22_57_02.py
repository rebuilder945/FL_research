lst= eval(input())
lst1=[]
for x in range(len(lst),-1,-1):
    if lst[x] not in lst1:
        lst1.append(lst[x])
print(lst1)
