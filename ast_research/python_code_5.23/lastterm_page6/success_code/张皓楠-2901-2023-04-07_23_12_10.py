b = []
a = input()
while a != "#":
    b.append(eval(a))
    a = input()
print(len(b),end=" ")
print(sum(b))

