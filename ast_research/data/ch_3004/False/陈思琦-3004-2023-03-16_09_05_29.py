a=eval(input())
b=[]
for x in a :
    if x > 3 and x not in b:
        for i in range(2,x):
            
                if x % i == 0:
                    break
                else:
                    b.append(x)
    elif x in b:
        continue
    elif 1<x<4:
        b.append(x)
print(b)
