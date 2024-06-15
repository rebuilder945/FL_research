a=eval(input())
b=[]
for x in a :
    if x not in b:
        for i in range(2,x//2):
            if x % i == 0:
                continue
            else:
                b.append(x)
    else:
        continue
print(b)
