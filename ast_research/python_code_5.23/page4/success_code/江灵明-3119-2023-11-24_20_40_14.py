a = eval(input());a=a[::-1]
b=[]
for i in a:
    if i not in b:
        b.insert(0,i)
        print(b)


