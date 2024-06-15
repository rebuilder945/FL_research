a=eval(input())
b=[]
for x in a :
    for i in range(2,x//2+1):
        if x not in b:
             if x % i == 0:
                break
             else:
                b.append(x)
        else:
            continue
print(b)
