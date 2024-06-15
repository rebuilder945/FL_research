dict1 = {}
lst = input().split()

for str1 in lst:
    dict1[str1] = dict1.get(str1,0) + 1
lst2 = []

for k,v in dict1.items():
    lst2.append([k,v])
lst2.sort(key = lambda x :x[1],reverse = True)
max_lst = list(dict1.values())
max_num = lst2[0][1]

if max_lst.count(max_num) >=1:
    num2 = max_lst.count(max_num)
    lst3 = []
    
    for i in range(num2):
        lst3 += lst2[i]
    lst3.sort(key = lambda x :x[0])    
    for t in lst3:
        k,v = lst(t)
        print(k,v)
else:
    k,v = lst2[0]
    print(k,v)
