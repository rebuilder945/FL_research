lst = eval(input())
lst1 = lst.copy()
lst2 = []
for x in lst:
    a = max(lst1)
    b = lst1.pop(a)
    lst2.append(b)
c = " "
for s in lst2:
    c += str(s)#  c += str(s) + ","这样写就让字符串之间以逗号相隔
print(c) 



