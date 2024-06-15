n = int(input("请输入一个整数："))
digits = str(n)
j = 1
b = -1
flag = False

while n > 0:
    if n % 10 == 5:
        print(j)
        j += 1
    n = n // 10
    j += 1

if '5' not in digits:
    print(b)
#尝试在一个整数 n 上使用 in 运算符，而整数不可迭代，因此无法进行 in 操作。
#通过将整数转换为字符串来解决这个问题，然后检查 '5' 是否在字符串中。