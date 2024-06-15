a=eval(input())
b=[]
for x in a:
    for i in range(x):
        if i>1:
            if x%i == 0:
                b.append(x)
for y in b:
    if y in a:
        a.remove(y)
if 0 in a:
    a.remove(0)
if 1 in a :
    a.remove(1)
print(a)


                

