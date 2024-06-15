a = input()
ls = []
while a != "q":
    ls.append(a)
    a = input()
dict = {}
for x in ls:
    dict[x] = ls.count(x)
ls2 = []
for k,v in dict.items():
    ls2.append([k,v])
ls2.sort(key=lambda x:x[1],reverse=True)
print(ls2[0][0],ls2[0][1])
