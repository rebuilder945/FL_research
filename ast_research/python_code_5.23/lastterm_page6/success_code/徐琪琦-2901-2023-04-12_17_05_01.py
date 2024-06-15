#从键盘不断地输入整数，当输入“#”时程序退出，然后打印出所输入整数的个数和总和。(题型：接收连续输入)
s = input()
lst = []
while s != "#":
    lst.append(s)
    s = input()
print(len(lst),sum(lst))
