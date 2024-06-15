ls = eval(input())
a = 0
b = 1
c = ls[a] + ls[b]
for i in range(len(ls)-1):
    b += 1
    c += ls[b] 
d = c/len(ls)
if d % 1 == 0:
    e = int(d)
    print(e)
else:
    print("%.2f"%d)

