string_list=list(input())
lst=[]
for x in string_list:
    if string_list.count(x)==1:
        lst.append(x)
if lst:
    print(lst[0])
else:
    print('None')
