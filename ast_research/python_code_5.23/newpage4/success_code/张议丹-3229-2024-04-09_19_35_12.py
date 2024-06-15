a = eval(input())
b = [x for x in a if a.count(x)==1]
c = sorted(b)
print(c)
