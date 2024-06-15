a=eval(input())
b=[x for x in range(a+1)]
b.remove(0)
c=b.pop(0)
b.append(c)

print(b)
