a=eval(input())
le=[x for x in range(1,a+1)]
b=le[0]
del le[0]
le.append(b)
print(le)

