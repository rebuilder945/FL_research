a = input() or "q"
dic = {}
while a != "q":
    if a in dic:
        dic[a] += 1
    else:
        dic[a] = 1
    a = input() or "q"
b = list(dic.values())
c = list(dic.keys())
x = b.index(max(b))
print(c[x],b[x])
