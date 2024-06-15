item = input() or "q"
ls = []
dic = {}
while item != "q":
    ls.append(item)
    item = input() or "q"
for x in ls:
    a = ls.count(x)
    dic[x] = str(a)
lst = []
for k,v in dic.items():
    lst.append([k,v])
lst.sort(key=lambda x:x[1],reverse=True)
print(lst[0][0],lst[0][1])



