def s(n):
    for i in range(2,n//2+1):
        if n % i ==0:
            return False
    return True
a = list(eval(input()))
b = []
for x in a:
    if s(x):
        b.append(x)
        while 1 in b:
            b.remove(1)
        
print(b)

