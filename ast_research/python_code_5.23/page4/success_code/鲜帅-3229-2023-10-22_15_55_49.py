ls1 = eval(input())
ls2 = []
for x in ls1:
    a = ls1.count(x)
    if a==1:
        ls2.append(x)
ls2.sort()
if ls2==[]:
    print("False")
else:
    print(",".join(str(x) for x in ls2))
