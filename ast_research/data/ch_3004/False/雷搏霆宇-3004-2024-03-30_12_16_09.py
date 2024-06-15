a = list(eval(input()))
b = []
def su(x):
    for i in range(2,x):
       if x % i == 0:
           return False
    return True
for i in a:
    if su(i):
        b.append(i)
print(b)



