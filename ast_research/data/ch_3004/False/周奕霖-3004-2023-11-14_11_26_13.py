b = eval(input())
c =[]
for x in b:
    for i in range(2,x):
        if x%i == 0:
            c.append(x)
b = [x for x in b if x not in c]
print(b)


        

