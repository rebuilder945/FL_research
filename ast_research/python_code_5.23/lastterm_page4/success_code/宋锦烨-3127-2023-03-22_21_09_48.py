a = int(input())
b = [x*1 for x in range(1,a+1)]
c =[]
for i in b:
    c.append(b[i-2])
print(c)

