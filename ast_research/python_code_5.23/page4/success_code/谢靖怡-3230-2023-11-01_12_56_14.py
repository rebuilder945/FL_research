ls=eval(input())
ls.sort(reverse=True)
lst1 = [str(i) for i in ls]
lst2 = ''.join(lst1)
lst2 = int(lst2)
print(lst2)
