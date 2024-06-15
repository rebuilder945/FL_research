def ss(n):
    if n >=2:
        for x in range(2,n):
            if (n%x == 0):
                return False
        else:
            return True
    else:
        return False
a = eval(input())
b = []
for y in a:
    if (ss(y)):
        b.append(y)
print(b)
