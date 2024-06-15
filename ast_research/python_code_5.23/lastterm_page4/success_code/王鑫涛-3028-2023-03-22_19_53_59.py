n = list(eval(input()))
a = n[0]
d = n[2]
c = n[1]
g = [a+i*d for i in range(c)]
print(g)
