m = input()
n = input()
lm = list(m)
ln = list(n)
for x in ln:
    while True:
        if x in lm:
            lm.remove(x)
        else:
            break
print(''.join(lm))
