lst=eval(input())
for i in lst:
    for x in range(2,i):
        if  i%x==0:
            lst.pop(i)
print(lst)

    
