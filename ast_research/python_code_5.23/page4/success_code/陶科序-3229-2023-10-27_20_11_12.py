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
for i in b:
    c += str(i)+""
print(c)


