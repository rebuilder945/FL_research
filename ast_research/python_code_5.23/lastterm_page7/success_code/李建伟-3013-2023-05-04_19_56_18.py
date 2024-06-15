lst = input().split()
dic = {}
while lst[0] != 'ok':
    dic[lst[0]] = int(lst[1])
    lst = input().split()
lst1 = []
for i in dic.keys():
    lst1.append(i)
lst1.sort()
print(lst1)
lst2 = []
for j in dic.values():
    lst2.append(j)
lst2.sort()
print(lst2)
if 'India' in lst1:
    print('yes')
else:
    print('no')
print(sum(lst2))
