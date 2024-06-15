lst = eval(input('请输入一个列表：'))
n, m = eval(input('请输入两个整数n和m，用逗号分隔：'))
n = int(n)
m = int(m)

if n < 0 or m > len(lst) or n >= m:
    print('error')
else:
    for x in range(n, m):
        del lst[x]
    print(lst)

