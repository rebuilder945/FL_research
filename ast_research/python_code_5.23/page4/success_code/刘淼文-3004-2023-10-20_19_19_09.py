l = eval(input())
l2 = []
for i in l:
    if i >= 2:
        for n in range(2,i,1):
            if i%n==0:
               break
        else:
            l2.append(i)
print(l2)

