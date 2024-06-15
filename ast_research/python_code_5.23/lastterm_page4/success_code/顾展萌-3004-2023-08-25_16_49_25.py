lst = eval(input())
lst1 =[]
for i in lst:
    for x in range(2,i) :
        if i % x ==0 or i == 1:
            break
    else:
        lst1.append(i)
print(lst1)

