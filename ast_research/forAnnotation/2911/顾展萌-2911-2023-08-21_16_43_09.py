a = list(input())
b = []
c = []

for i in range(len(a)):
    b.append(int(a[i])+5)
for i in range(len(b)):
    c.append(int(b[i]%10))
c.reverse()
print(str(c))
   

