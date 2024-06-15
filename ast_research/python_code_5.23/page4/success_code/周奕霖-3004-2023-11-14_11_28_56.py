b = eval(input())
c =[x for x in b if x > 1]
for x in b:
    for i in range(2,x):
        if x%i == 0:
            c.append(x)
b = [x for x in b if x not in c]
print(b)


        

