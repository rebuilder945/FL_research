a = eval(input())
b = []
for i in a:
    if a.count(i)==1:
        b.append(i)
if len(b)==0:
    print("False")
else:
    for i in b:
        print(i,end=",")
