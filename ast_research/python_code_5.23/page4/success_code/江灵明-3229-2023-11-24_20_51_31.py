a = eval(input());b=[]
for i in a:
    if a.count(i)==1:
        b.append(i)
if b==[]:
    print("False")
else:
    print(b.sort(reverse=False))

