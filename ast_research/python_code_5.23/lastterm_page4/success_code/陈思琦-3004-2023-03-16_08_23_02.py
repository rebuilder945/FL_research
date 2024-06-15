a=eval(input())
b=[]
for x in a :
    if x not in b:
        for i in range(2,x//2):
            if x % i == 0:
                break
            else:
                b.append(x)
print(b)
