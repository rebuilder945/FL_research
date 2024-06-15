__name__ = input("请输入一个字符串：")

name1 = 0
name2 = 0
name3 = 0
name4 = 0

for char in __name__:
    if "0" <= char <= "9":
        name1 += 1
    elif "a" <= char <= "z":
        name2 += 1
    elif char == " ":
        name3 += 1
    else:
        name4 += 1
#当你从输入中提取字符时，每个字符都是字符串类型，
#因此你不能直接与数字进行比较。你需要将字符转换为数字才能进行比较。

print(" ".join([str(name1), str(name2), str(name3), str(name4)]))