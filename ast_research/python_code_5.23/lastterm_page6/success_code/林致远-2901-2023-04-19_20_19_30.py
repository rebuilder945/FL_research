n = 0
l = []
while n != "#":
    n = input()
    if n!='#':
        n=int(n)
        l.append(n)
print(len(l),sum(l))
