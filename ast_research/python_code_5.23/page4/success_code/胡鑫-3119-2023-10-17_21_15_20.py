lst1 = eval(input())
lst2 = lst1.copy()
for x in lst1:
    cishu = lst2.count(x)
    if cishu > 1:
       while cishu >1:
            lst2.remove(x)
            cishu -= 1
print(lst2)
