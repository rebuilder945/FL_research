def shushu(i):
    for x in range(2,i//2+1):
        if i%x == 0:
            return False
    return True
lst = eval(input())
new = []
for x in lst:
    if shushu(x) and x >=2:
        new.append(x)
print(new)
