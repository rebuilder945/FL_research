n = eval(input())
lst1 = list(range(1,n+1))
lst2 = ['']
for i in lst1:
    if i == 1:
        lst2.insert(-2,1)
    else:
        lst2.insert(0,i)
lst2.pop()
print(lst2) 

