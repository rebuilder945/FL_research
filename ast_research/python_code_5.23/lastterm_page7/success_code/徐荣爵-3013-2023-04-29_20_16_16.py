str = input()
GDP = {}
while True:
    k,v = str.split()
    GDP[k] = GDP.get(k,0) + int(v)
    str = input()
    if str != 'ok':
        continue
    else:
        break
nation = list(GDP.keys())
num = list(GDP.values())
nation.sort()
num.sort()
sum1 = 0
for i in range(len(num)):
    sum1 += int(num[i])

print(nation)
print(num)
if 'India' in nation:
    print('yes')
else:
    print('no')
print(sum1)
