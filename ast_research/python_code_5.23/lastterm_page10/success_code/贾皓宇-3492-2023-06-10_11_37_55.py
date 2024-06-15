a=input()
lst=[]
for x in a:
    if a.count(x)==1:
        lst.append(x)
if lst==[]:
    print('None')
else:
    print(lst[0])
