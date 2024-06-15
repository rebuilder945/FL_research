list = eval(input())
alpha = ""
for i in list:
    alpha += i
a = []
for i in alpha:
    if i not in a:
        a.append(i)
a.sort()
for i in a:
    b = alpha.count(i)
    print("%s\,%d"%(i,b))
