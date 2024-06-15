a = eval(input())
b = []
for x in a :
    if x < 2 :
        b.append(x)
    else:
        for i in range(2,x):
            if x % i ==0:
                break
        else:
                b.append(x)
if  1 in b:
    b.remove(1)
if 0 in b:
    b.remove(0)
print(b)
