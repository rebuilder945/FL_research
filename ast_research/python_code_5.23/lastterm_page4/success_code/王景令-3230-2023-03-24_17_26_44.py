a = eval(input())
c = ''
for i in range(len(a)):
    b = a.pop(max(a))
    if str(b) not in c:
        c = c + str(b)
    else:
        continue
print(int(c))
