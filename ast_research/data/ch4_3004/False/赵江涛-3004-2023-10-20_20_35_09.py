ls = eval(input())
for x in ls :
    if x == 1:
        ls.remove(x)
    elif x ==0:
        ls.remove(x)
    else:
            for j in range(2,x):
                if x%j ==0:
                    ls.remove(x)
                    break
        
print(ls)

