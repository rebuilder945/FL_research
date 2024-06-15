a = ''
name = []
num = name.copy()
while True:
    if a != 'ok':
        a = input().split()
        name.append(a[0])
        num.append(int(a[1]))
    else:
        break
print(name.sort())
print(num.sort())
if 'India' in name:
    print('yes')
else:
    print('no')
print(sum(num))
