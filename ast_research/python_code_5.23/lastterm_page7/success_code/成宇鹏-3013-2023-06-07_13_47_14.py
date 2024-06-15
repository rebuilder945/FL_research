a = input() or "ok"
dic = {}
while a != "ok":
    b = a.split()
    dic[b[0]] = int(b[1])
    a = input() or "ok"
n = list(dic.keys())
n.sort()
m = list(dic.values())
m.sort()
c = sum(m)
print(n)
print(m)

if "India" in dic:
    print("yes")
else:
    print("no")
print(c)

