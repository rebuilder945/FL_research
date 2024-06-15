str1=input()
lst=[]
for x in str1:
    if str1.count(x)==1:
        lst.append(x)
if len(lst)==0:
    print('None')
else:
    print(lst[0])


