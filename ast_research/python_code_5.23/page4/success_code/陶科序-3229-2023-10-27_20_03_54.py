a = eval(input())
b = []
for i in a:
    if a.count(i) == 1:
        b.append(i)
    else:
        continue
if b == []:
    print("False")
else:
    print(str(b))
