ls = eval(input())
ls1 = []
for x in ls:
    if ls.count(x)==1:
        ls1.append(x)
if len(ls1)==0:
    print("False")
else:
    ls1.sort()
    for x in ls1:
        print(x, end=",")
