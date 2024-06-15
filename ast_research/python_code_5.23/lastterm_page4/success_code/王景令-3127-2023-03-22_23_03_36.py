a = eval(input())
b = [x+1 for x in range(a)]
c = []
for x in b:
    c.insert(x%n,n)
print(c)
    
