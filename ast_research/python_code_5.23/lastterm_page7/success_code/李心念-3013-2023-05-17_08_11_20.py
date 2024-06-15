a = ''
name = []
num = name.copy()
while a != 'ok':
    a = input().split()
    name.append(a[0])
    num.append(int(a[1]))
print(name)
print(num)
if 'India' in name:
    print('yes')
else:
    print('no')
print(sum(num))
