lst = eval(input())
l2 = []
for i in lst:
    if i >= 2:
        for x in range(2,i):
            if i % x == 0:   
                break
            else:
                l2.append(i)
print(l2)

