ls = eval(input())
a = 0
b = 1
c = ls[a] + ls[b]
for i in range(1,len(ls)-1):
    b += 1
    c += ls[b] 
d = c/len(ls)
print("%.2f"%d)
