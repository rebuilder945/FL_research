b = eval(input())
c =[x for x in b if x > 1]
d = []
for x in b:
    for i in range(2,x):
        if x%i == 0:
            d.append(x)
o = [x for x in b if x not in d and x > 1]
print(o)


        

