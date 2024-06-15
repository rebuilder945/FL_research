m = input()
n = input()
lm = list(m)
ln = list(n)
for x in ln:
    while True:
        if x in la:
            la.remove(x)
        else:
            break
print(''.join(la))
