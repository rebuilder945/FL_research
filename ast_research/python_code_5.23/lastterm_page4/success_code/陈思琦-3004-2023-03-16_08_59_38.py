a=eval(input())
b=[]
for x in a :
    if x > 3:
        for i in range(2,(x**1/2)+1):
            if x not in b:
                if x % i == 0:
                    break
                else:
                    b.append(x)
            else:
                continue
    elif 1<x<4:
        b.append(x)
print(b)
