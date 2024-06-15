s = input().split(' ')
dic = {}
for i in s:
    n = s.count(i)
    dic[i] = n
dic1 = {}
for key,value in dic.items():
    if value == max(dic.values()):
        dic1[key] = value
sorted(dic1.items())
for key1,value1 in dic1.items():
    print(key1,value1)
