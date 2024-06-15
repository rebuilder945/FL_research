a=eval(input())
b=[]
for i in a:
    if a.count(i)==1:
        b.append(i)
        print(b)
else:
    print(False)

