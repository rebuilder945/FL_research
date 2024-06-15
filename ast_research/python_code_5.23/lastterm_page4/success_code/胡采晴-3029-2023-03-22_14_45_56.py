a = input()
b = eval(input())
c = a.split(",")
d = int(len(c))
e = []
for i in range(d):
    e.append([c[i]],b[i])
print(e)
