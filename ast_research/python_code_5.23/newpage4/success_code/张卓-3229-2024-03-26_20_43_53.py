a = list(eval(input()))
b=[]
a.sort()
for i in a:
    if a.count(i) == 1:
        b.append(i)
if b==[]:
    print("False")
else:
    for s in b:
        if b[-1] in [s]:
            print(s,end="")
        else:
            print(s,end=",")



