item = input()
ls = []
ls2 = []
dic = {}
money = 0
while item != "ok":
    a,b = map(str,item.split(" "))
    dic[a] = b
    item = input()
for i in dic.keys():
    ls.append(i)
    money += int(dic[i])
print(sorted(ls))
for i in dic.values():
    ls2.append(i)
print(sorted(ls2))
if "India" in dic.keys():
    print("yes")
else:
    print("no")
print(money)



