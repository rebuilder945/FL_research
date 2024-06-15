a = eval(input())
n = 0
b = []
c = []
for x in a:
    if x  not in b:
        b.append(x)
        if x  in b:
            c.append(x)
            n+=1
if n:
    print(c)
else:
    print("False")
