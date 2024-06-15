dict1 = {}
lst = input().split()

for str1 in lst:
    dict1[str1] = dict1.get(str1,0) + 1
lst2 = []

for k,v in dict1.items():
    lst2.append([k,v])
lst2.sort(key = lambda x :x[1],reverse = True)

max_num = lst2[0][1]
lst3 = []
for i in range(len(lst2)):
    if lst2[i][1] == max_num:
        lst3 += [lst2[i]]
    else:
        break
if len(lst3) == 1:
    k,v = lst3[0]
    print(k,v)
else:
    lst4 = []
    for i in range(len(lst3)):
        lst4 += [lst3[i][0]]
    lst4.sort()
    for i in lst4:
        print(i,max_num)


