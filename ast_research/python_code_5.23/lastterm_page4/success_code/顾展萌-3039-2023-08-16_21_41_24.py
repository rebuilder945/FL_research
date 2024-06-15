m = eval(input())
n = m.sort(reverse = True)
x = n.remove(n[-1])
del n[x,]
p = n.sort(reverse = False)
y = p.remove(p[-1])
del p[y,]
print(p)



    












