a = eval(input())
c = ''
while len(a) > 0:
    b = str(a.pop(max(a)))
    if b not in c:
        c = c + str(b)
    else:
        continue
print(int(c))
