let = 0
spa = 0
num = 0
oth = 0
pStr = str(input())
for i in pStr:
    if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
        let += 1
    elif 48 <= ord(i) <= 57:
        num += 1
    elif ord(i) == 32:
        spa += 1
    else:
        oth += 1
print('{} {} {} {}'.format(let, spa, num, oth))
