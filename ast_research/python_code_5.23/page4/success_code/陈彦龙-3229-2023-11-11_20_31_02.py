lst1 = eval(input())
lst2 = [x for x in lst1 if lst1.count(x) == 1]
print(",".join(str(lst2)))
if lst2 !=[]:
    lst2.sort()
    print(",".join(str(x) for x in lst2))
else:
    print(False)

        

