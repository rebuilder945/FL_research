ls1 = eval(input())
ls2 = []
for i in ls1:
    for x in range(2,i-1):
        if i/x==0:
            ls2.append(i)
print(ls2)
