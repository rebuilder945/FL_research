a = list(eval(input()))
b = []
def su(x):
    if x <= 1:
        return False
    for i in range(2,x//2+1):
       if x % i == 0:
           return False
    return True
for i in a:
    if su(i):
        b.append(i)
print(b)



