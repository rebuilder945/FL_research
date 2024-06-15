a = list(eval(input()))
b = []
c = []
for i in a:
    t = a.count(i)
    if t == 1:
        b.append(i)
        b.sort()
if b == c:
    print("False")
else:
    for s in b:
        if b[-1] in [s]:
            print(s,end="")
        else:
            print(s,end=",")


