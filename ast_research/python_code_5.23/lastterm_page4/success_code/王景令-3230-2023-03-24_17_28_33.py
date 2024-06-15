a = eval(input())
c = ''
while len(a) > 0:
    b = a.pop(max(a))
    if str(b) not in c:
        c = c + str(b)
    else:
        continue
print(int(c))
