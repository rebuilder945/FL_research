lst=list(input())
lst2=[]
for i in lst:
    if lst.count(i)==1:
        lst2.append(i)
        break
if len(lst2)==1:
    print(lst2[0])
else:
    print("None")
