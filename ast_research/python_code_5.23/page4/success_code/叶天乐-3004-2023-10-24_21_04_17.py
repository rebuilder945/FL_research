ls1 = eval(input())
for i in ls1:
    for m in range(2,i//2+1):
       if i%m ==0:
           ls1.remove(i)
       else:
        pass
print(ls1)
