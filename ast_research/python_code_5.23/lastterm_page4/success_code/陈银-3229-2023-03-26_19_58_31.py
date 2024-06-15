a = eval(input())
c = []
for i in a:
    if a.count(i) == 1:
        c.insert(0,i)
        c.sort()
    else:
        c = str("False")
print(c)
    
    
