a = input()
b = []
while (a != "#" ):
    b.append(int(a))
    a = input()
l = len(b)
s = sum(b)
print(l,s)
