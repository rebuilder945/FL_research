a=input()
a=a.strip("[")
a=a.rstrip("]")
b=[int(i) for i in a.split(",")]
n=b.count(0)
for i in range(int(n)):
    b.remove(0)
for i in range(int(n)):
    b.append(0)
print(b)
