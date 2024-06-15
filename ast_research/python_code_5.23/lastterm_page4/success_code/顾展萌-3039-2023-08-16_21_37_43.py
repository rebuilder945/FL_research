m = eval(input())
n = m.sort(reverse = True)
x = n.index(n[-1])
del n[x,]
p = n.sort(reverse = False)
y = p.index(p[-1])
del p[y,]
print(p)



    












