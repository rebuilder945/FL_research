ls=eval(input())
for i in ls:
    if i ==1:
        ls.remove(i)
    if i != 2 and i != 3:
       for x in range(2,i):
           if i%x==0:
               ls.remove(i)


print(ls)



