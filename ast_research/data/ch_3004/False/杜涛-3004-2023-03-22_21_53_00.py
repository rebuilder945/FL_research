a=eval(input())
c=[2]
for x in a:
    for i in range(2,x):

        if x%i!=0:
            c.append(x)
            break
print(c)


