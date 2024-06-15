a = input().split(',')
b = []
def abc(a):
    for i in range(2,a):
        if a % i == 0:
            return False
for i in a:
    i = int(i)
    if abc(i) == False:
        continue
    else:
        b.append(i)
print(b)



