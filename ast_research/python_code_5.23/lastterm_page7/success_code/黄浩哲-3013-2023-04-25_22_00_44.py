dic = {}
while True:
    n = input()
    if n == 'ok':
        break
    else:
        lst = n.split(' ')
        dic[lst[0]] = int(lst[1])
lst1 = list(dic.keys())
lst2 = list(dic.values())
lst1.sort()
lst2.sort()
print(lst1)
print(lst2)
if 'India' in dic:
    print('yes')
else:
    print('no')
print(sum(lst2))


