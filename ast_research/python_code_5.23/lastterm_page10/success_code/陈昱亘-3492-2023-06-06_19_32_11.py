string=input()
if string != '':
    lst=list(string)
    lst2=[]
    for i in lst:
        if lst.count(i)==1:
            lst2.append(i)
    print(lst2[0])
else:
    print('None')
