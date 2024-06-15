ls = eval(input())
for x in ls:
    n = ls.count("x")
    for i in range(n-1):
        ls.remove(x)
    print(ls)    
