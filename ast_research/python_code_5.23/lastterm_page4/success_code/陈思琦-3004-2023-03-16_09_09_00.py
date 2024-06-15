a=eval(input())
b=[]
for x in a :
    if x > 3:
        for i in range(2,x):
            if x not in b :
                if x % i == 0:
                    continue
                else:
                    b.append(x)
    elif x in b:
        continue
    elif 1<x<4:
        b.append(x)
print(b)
