a = eval(input())
a.sort()
i = 0
s = 0
for k in a:
    k = k*10**i
    s = k + s
    i = i + 1
print(s)


    



    
