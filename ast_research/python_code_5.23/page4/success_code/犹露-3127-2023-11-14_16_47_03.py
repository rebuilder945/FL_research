a = eval(input())
c = [x for x in range(1,a+1)]
for i in range(a):
    c[i-1],c[i] = c[i],c[i-1]
print(c)







