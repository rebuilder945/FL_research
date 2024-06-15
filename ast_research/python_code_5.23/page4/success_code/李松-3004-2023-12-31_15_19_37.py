A = eval(input())
b = []
def abc(a):
    for i in range(2,a):
        if a % i == 0:
            return False
for i in A:
    if abc(i) == False:
        continue
    else:
        b.append(i)
if 0 in b:
    b.remove(0)
if 1 in b:
    b.remove(1)
print(b)





