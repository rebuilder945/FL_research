a = 1 
b = 2
n = eval(input())
c = 0
ls = []
while c < n:
    ls.append(b/a)
    b = b + a
    a = b - a
    c += 1
sum = sum(ls)
print("%.4f"%(sum))

