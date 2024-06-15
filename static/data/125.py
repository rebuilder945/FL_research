ls = list(input())
a = 0
b = 0
c = 0
d = 0
for x in ls:
    if x.isalpha():  # 检查是否是字母
        a += 1
    elif x == " ":
        b += 1
    elif x.isdigit():  # 检查是否是数字
        c += 1
    else:
        d += 1
#错误出现在 eval(x) 这一行，因为 x 是一个字符串，而 eval() 函数期望接收一个表示有效Python表达式的字符串。
#由于 x 是一个单个字符的字符串，eval(x) 会尝试将它转换为整数，但是由于字符可能不是有效的数字字符，所以会引发错误。
print(a, b, c, d)