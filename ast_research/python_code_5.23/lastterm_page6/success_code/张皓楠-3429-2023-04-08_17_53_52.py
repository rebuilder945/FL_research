a = input()
b = 0
c = 0
d = 0
e = 0
for i in a:
    if ord(i) in range(97,123)+range(65,91):
        b += 1
    elif ord(i) == 32:
        c += 1
    elif ord(i) in range(48,58):
        d += 1
    else:
        e +=1
print(b,end=" ")
print(c,end=" ")
print(d,end=" ")
print(e)

