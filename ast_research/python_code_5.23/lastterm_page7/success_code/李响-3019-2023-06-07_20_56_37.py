a = {}
while True:
    i = input()
    if i == 'q':
        break
    if i not in a:
        a[i] = 1
    else:
        a[i] += 1
for k,v in a.items():
    if v == max(a.values()):
        print(k,v)

