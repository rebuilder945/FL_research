a=eval(input())
b=list(range(1,a+1))
c=b[0]
b.remove(c)
b.append(c)
print(b)
