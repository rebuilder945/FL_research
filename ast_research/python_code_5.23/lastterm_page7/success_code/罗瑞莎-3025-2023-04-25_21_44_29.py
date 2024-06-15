s = input().split(' ')
dic = {}
for i in s:
    n = s.count(i)
    dic[i] = n
dic1 = {}
for key,value in dic.items():
    if value == max(dic.values()):
        dic1[key] = value
lst = sorted(dic1)
for key1 in lst:
    print(key1,dic1[key1])
