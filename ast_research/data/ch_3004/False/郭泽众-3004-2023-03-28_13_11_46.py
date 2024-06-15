lst1 = eval(input())
lst2 = []
for i in lst1:
    for j in range(2,i):
        if i%j==0:
            break
    else:
        lst2.append(i)
print(lst2)
