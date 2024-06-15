# 从键盘不断地输入整数，当输入“#”时程序退出，然后打印出所输入整数的个数和总和。

lst = []
n = 1
b = input()
while str(b) != "#":
    lst.append(b)
    n += 1
    b = input()
lst1 = list(map(int,lst))
s = sum(lst1)
print(s)
print(n)

