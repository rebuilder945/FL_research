lst = eval(input())
lst.sort(reverse=True)
lst1 = [str(i) for i in lst]
lst2 = ''.join(lst1)
lst2 = int(lst2)
print(lst2)
