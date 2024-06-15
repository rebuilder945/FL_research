a = eval(input())
if sum(a) % len(a) == 0:
    print("%d" % (sum(a) / len(a)))
else:
    print(f'{sum(a) / len(a):.2f}')
    #在 print() 函数中的格式化字符串中存在语法错误。在 else 分支中的格式化字符串中有一个括号位置不正确的问题。