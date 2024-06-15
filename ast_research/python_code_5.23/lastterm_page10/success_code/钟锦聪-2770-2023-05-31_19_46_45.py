a = input()
b = input()
A =[]
B =[]
for x in a:
    A.append(x)
for y in b:
    B.append(y)
for x in a:
    B.remove(x)
if B ==[]:
    print("True")
else:
    print("False")

