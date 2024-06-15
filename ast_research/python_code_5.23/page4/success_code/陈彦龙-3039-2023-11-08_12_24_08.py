lst1 = eval(input())
Max = max(lst1)
Min = min(lst1)
lst2 = []
for x in lst1:
    if x !=Max and x !=Min:
        lst2.append(x)
print(lst2)    

