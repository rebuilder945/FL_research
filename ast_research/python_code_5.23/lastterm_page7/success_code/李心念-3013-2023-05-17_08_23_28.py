a = ''
name = []
num = name.copy()
while True:
    a = input()
    if a != 'ok':
        b = a.split()
        name.append(b[0])
        num.append(int(b[1]))
    else:
        break
print(sorted(name))
print(sorted(num))
if 'India' in name:
    print('yes')
else:
    print('no')
print(sum(num))
