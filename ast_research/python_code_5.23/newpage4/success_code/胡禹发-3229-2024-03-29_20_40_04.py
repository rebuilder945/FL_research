a=list(eval(input()))
b=[]
for i in a:
    if a.count(i)==1:
        b.append(i)
b.sort()
for i in b[:-1]:
        print(i,end=",")
if b==[]:
    print("false")
else:
    print(b[-1])
