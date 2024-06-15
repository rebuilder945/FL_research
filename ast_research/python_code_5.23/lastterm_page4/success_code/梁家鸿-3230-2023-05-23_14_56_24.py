a = eval(input())
a.sort(reverse = True)
c = []
for i in range(len(a)):
    b = a[i]*(10**(len(a)-i))
    c.append(b)
print(sum(c))
