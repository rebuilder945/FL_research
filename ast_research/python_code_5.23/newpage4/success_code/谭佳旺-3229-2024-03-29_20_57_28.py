a =eval(input())
b =[]
for i in a:
    if a.count(i)==1:
        b.append(i)
b.sort()
if b:
    print(",".join(str(c) for c in b))
else:
    print("False")

    



