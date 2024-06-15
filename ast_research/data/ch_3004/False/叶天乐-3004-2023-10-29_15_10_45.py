ls1 = eval(input())
ls2 = []
for i in ls1:
    for m in range(2,i//2+1):
       if i%m == 0:
           continue
       else:
        ls2.append(i)
print(ls2)


