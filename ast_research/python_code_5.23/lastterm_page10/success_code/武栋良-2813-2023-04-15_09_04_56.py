m = input()
n = input()
la = list(m)
while True:
    if n in la:
        la.remove(n)
    else:
        break
print(''.join(x for x in la))
