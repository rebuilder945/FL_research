lst = eval(input())
lst1 = []
for i in lst:
    if lst.count(i)==1:
        lst1.append(i)
if len(lst1):
    lst1.sort(reverse=False)
    print(*lst1,sep=',')
else:
    print('False')
