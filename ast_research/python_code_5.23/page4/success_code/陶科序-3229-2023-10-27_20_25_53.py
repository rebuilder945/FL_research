a = eval(input())
b = []
c = ""
for i in a:
    if a.count(i) == 1:
        b.append(i)
    else:
        continue
if b == []:
    print("False")
else:
    b.sort()
    for i in b[:-1]:
        c +=str(i)+","
    d = c+str(b[-1])
    print(d)




