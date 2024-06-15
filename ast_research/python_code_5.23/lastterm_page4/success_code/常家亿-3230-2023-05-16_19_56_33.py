lst = eval(input())
lst1 = lst.copy()
lst2 = []
for x in lst:
    a = max(lst1)
    lst1.remove(a)
    lst2.append(a)
c = " "
for s in lst2:
    c += str(s)#  c += str(s) + ","这样写就让字符串之间以逗号相隔
print(c) 



