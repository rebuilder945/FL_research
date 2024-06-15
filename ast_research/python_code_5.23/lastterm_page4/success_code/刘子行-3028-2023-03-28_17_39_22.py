n,m,l,=eval(input())
shit=[n]
for x in range(m-1):
    shit.append(shit[-1]+l)
print(shit)
