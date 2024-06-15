a = input().spilt(',')
b = eval(input())
c = list(a)
d = ()
e = []
for i in range(len(b)):
    d = (c[i],b[i])
    e.append(list(d))
print(e)
