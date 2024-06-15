lst=eval(input())
lst1=[]
for i in lst:
    if lst.count(i)<2:
        if i not in lst1:
            lst1.append(i)
lst1.sort()
if lst1==[]:
    print('False')
if len(lst1)>1:
    lst2=''
    for i in lst1:
        lst2+=str(i)+','
    print(lst2[0:-1])


