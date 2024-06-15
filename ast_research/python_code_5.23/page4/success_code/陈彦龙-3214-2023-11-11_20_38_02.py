lst1 = eval(input())
lst2 = [x for x in lst1 if x !=0]
n = len(lst1)-len(lst2)
lst3 = lst2 + [0] * n
print(lst3)
