lst1 = eval(input())
lst2 = []
for i in lst1:
    if lst1.count(i) == 1:
            lst2.append(i)
if len(lst2) == 0:
         print("False")
else:
    lst2.sort()  
    print(lst2)


