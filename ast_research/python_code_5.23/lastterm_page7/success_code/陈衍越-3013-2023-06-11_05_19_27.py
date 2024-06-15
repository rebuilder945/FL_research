GDP = {}
while True:
    #line = input().strip()
    #注意不能使用split(),与ok冲突
    line = input()
    if line == 'ok':
        break
    else:
        #创建键值对
        key,value = line.split()
        GDP[key] = eval(value)

lst1 = sorted(list(GDP.keys()))
lst2 = sorted(list(GDP.values()))
print(lst1)
print(lst2)
print('yes' if 'India' in lst1 else 'no')
print(sum(lst2))


