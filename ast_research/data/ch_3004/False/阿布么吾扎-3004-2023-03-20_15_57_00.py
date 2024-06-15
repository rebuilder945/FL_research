lst1 = eval(input())
lst2 = []
for n in lst1:
    for x in range(2,n//2+1):
        if n%x==0:
            lst2.append(n)
print(lst2)            

