lst1=eval(input())
lst2=sorted(set(lst1))
del lst2[0]
del lst2[-1]
print(lst2)
