a = input("请输入一个数值:")
b = input("请再输入一个数值:")
c = input("请再再输入一个数值:")
max = 0
if a > b:
    if a > c:
        max = a
    else:
        max = c
else:
    if b > c:
        max = b
    else:
        max = c
print("最大值为:" + max )
