a = input()
b = 0
for i in a:
    if i.isnumeric():
        b += 1
        break
for i in a:
    if 'a' <= 'i' <= 'z':
        b += 1
        break
for i in a:
    if 'A' <= i <= 'Z':
        b += 1
        break
if len(a) >= 8:
    b += 1
for i in a:
    if i in '~!@#$%^&*()_=-/,.?<>;:[]{}|\\':
        b += 1
        break
print(b)
        
