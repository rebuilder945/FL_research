ls = eval(input())
ls1 = []
for i in ls:
    if i>=2:
        for x in range(2,i,1):
            if i%x==0:
                break
        else:
            ls1.append(i)
            
print(ls1)               

