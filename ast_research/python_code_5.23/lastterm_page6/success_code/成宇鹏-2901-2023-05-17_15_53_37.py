# 从键盘不断地输入整数，当输入“#”时程序退出，然后打印出所输入整数的个数和总和。

lst = []
n = 0
b = input()
while str(b) != "#":
    lst.append(b)
    b = input()
    n += 1
lst1 = list(map(int,lst))
s = sum(lst1)
print(n,s)


