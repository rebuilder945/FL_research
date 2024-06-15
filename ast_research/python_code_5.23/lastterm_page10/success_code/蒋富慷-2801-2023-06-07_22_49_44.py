a = input()
b = 0
for i in a:
    if i.isdigit():
        b+=1
        break
for i in a:
    if i.islower():
        b+=1
        break
for i in a:
    if i.isupper():
        b+=1
        break
if len(a)>=8:
    b+=1
for i in a:
    if i in '~!@#$%^&*()_\=-/,.?<>;:[]}{|':
        b+=1
        break
print(b)
