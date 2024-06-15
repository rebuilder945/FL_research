def susu(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

a = eval(input())
b = []
for x in a:
    if susu(x):
        b.append(x)

print(b)

