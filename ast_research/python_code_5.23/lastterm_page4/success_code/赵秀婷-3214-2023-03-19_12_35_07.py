Li=eval(input())
x=Li.count(0)
p=0
while p < x:
    Li.remove(0)
    p += 1
q=0
while q < x:
    Li.append(0)
    q += 1
print(Li)
