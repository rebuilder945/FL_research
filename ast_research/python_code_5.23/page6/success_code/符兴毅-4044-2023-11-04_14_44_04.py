num = eval(input())
lis = []
for x in range(100, num + 1):
    str_num = str(x)
    sum = 0
    for i in str_num:
        sum += int(i) ** 3
    if sum == x:
        lis.append(x)
if len(lis) == 0:
    print('none')
else:
    for i in lis:
        print(i)

