n = eval(input())
for x in n:
    if n.count(x)>1:
        n.remove(x)
print(n)
