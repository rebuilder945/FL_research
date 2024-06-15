ls = eval(input())
ls2 = []
for x in ls :
    for j in range(2,x):
        if x%j ==0:
            ls.remove(x)
            break
        
print(ls)

