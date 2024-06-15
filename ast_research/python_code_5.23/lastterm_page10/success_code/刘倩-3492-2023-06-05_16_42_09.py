a = input()

if len(s) == 0:
    print("None")
else:
    found = False
    for x in a:
        if a.count(x) == 1:
            print(x)
            found = True
            break

    if not found:
        print("None")



#`if not s` 是一个条件判断语句，用于判断变量 `s` 是否为空。在这里，`not` 是一个逻辑运算符，用于对条件取反。\
# 如果 `s` 是一个空字符串，即长度为 0 的字符串，则 `not s` 的结果为 `True`，表示条件成立。反之，如果 `s` 不是空字符串，则 `not s` 的结果为 `False`，表示条件不成立。
#因此，`if not s` 可以用来检查输入的字符串是否为空。如果输入的字符串为空，即长度为 0，则条件成立，执行相应的代码块，打印 "None"。如果输入的字符串不为空，则条件不成立，执行其他代码块。
#总结起来，`if not s` 用于判断字符串 `s` 是否为空，是一种简洁的写法。
