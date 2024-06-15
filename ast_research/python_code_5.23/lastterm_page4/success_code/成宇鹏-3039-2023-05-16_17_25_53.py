lst = eval(input())
lst1 = list(set(lst))

lst1.remove(max(lst1))
lst1.remove(min(lst1))
print(lst1)
