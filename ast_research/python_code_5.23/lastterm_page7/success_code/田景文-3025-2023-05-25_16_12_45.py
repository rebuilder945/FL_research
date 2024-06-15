ls = list(input().split())
dic = {}
for x in ls:
    dic[x] = ls.count(x)
s = []
a = max(dic.values())
for x in dic.keys():
    if dic[x] == a:
        s.append(x)
s.sort()
for x in s:
    print(f"{x} {a}")
