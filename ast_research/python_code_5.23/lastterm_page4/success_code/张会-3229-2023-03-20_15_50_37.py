lst1 = eval(input())
lst2 =[]
for i in range(len(lst1)-1):
    if lst1.count(i)==1:
        lst2.append(i)
        lst2.sort()
if lst2 == []:
    print(False)
else:
    print(*lst2,sep =',')

