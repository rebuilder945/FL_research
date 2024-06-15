a = input("请输入：")
dit = {}
lst = []
while a!= "q":
    lst.append(a)
    a = input()
for x in lst:
    b = lst.count(x)
    dit[x] = b
d = list(dit.keys())
e = list(dit.values())
f = int(max(e))
g = e.index(f)
h = d[g]
print(h,f)





