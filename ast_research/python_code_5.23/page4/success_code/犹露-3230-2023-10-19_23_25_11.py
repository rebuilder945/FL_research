a = eval(input())
a.sort()
d =[]
for i in range(len(a)):
    b = a[i]
    c = b*10**(i)
    d.append(c)
    m = sum(d)
print(m)
# b.append(a)
# print(b)




