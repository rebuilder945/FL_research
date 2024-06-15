m = input()
n = input()

while True:
    if n in m:
        m.remove(n)
    else:
        break
print(m)
