n = 0
s = 0
while True:
    a = input().strip()
    if a=='#':
        break
    else:
        n+=1
        s+=int(a)

print(f"{n} {s}")
