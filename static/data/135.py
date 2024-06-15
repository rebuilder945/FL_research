n = eval(input())
for i in range(100, n+1):
    b = i // 100
    b1 = i % (b * 100)
    s = b1 // 10
    s1 = b1 - (s * 10)
    if i == b ** 3 + s ** 3 + s1 ** 3:
        print(i)
if n < 100:
    print("none")
#使用了错误的循环方式。
#应该使用 range() 函数来生成一个范围内的数字序列进行迭代，而不是直接用元组构成的迭代对象。