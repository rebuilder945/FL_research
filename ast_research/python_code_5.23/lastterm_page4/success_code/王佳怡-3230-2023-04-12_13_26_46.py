l=list(eval(input()))
l.sort()
a=""
for i in range(len(l)):
    a+=str(l[i])
print(int(a))
