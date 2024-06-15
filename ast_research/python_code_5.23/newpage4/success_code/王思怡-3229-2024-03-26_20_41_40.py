a = list(eval(input()))
b = []
c = []
for i in a:
    if a.count(i) ==1:
        b.append(i)
    else:
        c.append(i)
b.sort()
if b == []:
    print("False")
else:
    print(b)

        

