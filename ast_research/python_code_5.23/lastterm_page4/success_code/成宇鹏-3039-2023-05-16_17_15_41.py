lst = eval(input())
lst1 = list(set(lst))
del lst1[0]
del lst1[len(lst1)-1]
print(lst1)
