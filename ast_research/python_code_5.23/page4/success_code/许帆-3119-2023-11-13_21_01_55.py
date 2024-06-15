lst1 = eval(input())
for a in lst1:
    for x in range(lst1.count(a)-1):
        lst1.remove(a)
    
print(lst1)


