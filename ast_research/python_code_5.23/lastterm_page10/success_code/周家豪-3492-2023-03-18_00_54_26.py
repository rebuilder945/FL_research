string=input()
lst=[]
k=0
for x in string:
    lst2=[]
    lst2.append(x)
    lst2.append(string.count(x))
    lst.append(lst2)
for i in range(len(lst)):
    if lst[i][1]==1:
        print(lst[i][0])
        k=1
        break
if k==0:
    print('None')


