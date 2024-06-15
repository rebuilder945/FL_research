a = eval(input())
b=max(a)
c=min(a)
a=list(set(a))
a.remove(b)
a.remove(c)
print(a)






