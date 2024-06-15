a = eval(input())
b = [x+1 for x in range(a)]
c = [x for x in b[1:]] + [1]
print(c)
    
