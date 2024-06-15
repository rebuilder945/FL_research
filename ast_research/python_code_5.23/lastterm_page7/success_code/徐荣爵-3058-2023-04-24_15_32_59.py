from re import T


str1 = str(input())
dict1 = {}
while str1 != 'q':

    dict1[str1] = dict1.get(str1,0) + 1
    str1 = str(input())
lst = []

for k,v in dict1.items():
    lst.append([k,v])
lst.sort(key = lambda x :x[1],reverse = True)
p,q = lst[0]
print(p,q)

