a = list(eval(input()))
print(a)
b = eval(input())
c = []
for i in range(len(a)): 
    print(i)
    c.extend([a[i],b[i]])
print(c)

