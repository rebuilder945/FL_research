a = input()
b = input()
c = ''
while True:
    if a.find(b) != -1:
        a = a[:a.find(b)] +a[a.find(b)+len(b):]
    else:
        break
print(a)
