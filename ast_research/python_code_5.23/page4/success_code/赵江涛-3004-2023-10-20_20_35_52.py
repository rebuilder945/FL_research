ls = eval(input())
for x in ls :
    if x ==1:
        ls.pop(x)
    elif x ==0:
        ls.pop(x)
    else:
            for j in range(2,x):
                if x%j ==0:
                    ls.pop(x)
                    break
        
print(ls)

