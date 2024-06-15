ls=eval(input())
ls1=ls[:]
for i in ls1:
    if i == 0 or i == 1:
        ls.remove(i)
    if i != 2 and i != 3:
        for x in range(2,i):
           if i%x==0:
                ls.remove(i)
                break


print(ls)



