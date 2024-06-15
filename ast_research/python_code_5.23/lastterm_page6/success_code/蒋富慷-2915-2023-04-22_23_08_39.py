flag = 0
number = int(input())
for i in range(2,number+1):
    a = i
    temp = 0
    while i != 0:
        temp += (i % 10) ** 3
        i = i // 10
    if a == temp:
        print(a)
        flag = 1
if flag == 0:
    print('none')
