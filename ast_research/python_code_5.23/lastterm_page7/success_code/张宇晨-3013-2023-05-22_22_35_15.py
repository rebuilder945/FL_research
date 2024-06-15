dic = {}
a = ""
while a!="ok":
    a = input()
    if a!="ok":
        x,y = a.split(" ")
    else:
        break
    dic[x]=y

lst1 = sorted(list(dic.keys()))
print(lst1)
lst2 = sorted(list(map(int,dic.values())))
print(lst2)
if dic.get("India",False):
    print("yes")
else:
    print("no")
print(sum(lst2))
