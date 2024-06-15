a = eval(input())
a.sort(reverse=True)
b = []

for x in a:
    if str(x) not in b:
    #在比较之前确保进行类型转换，以确保所有要比较的数据具有相同的类型。通过在比较之前将 x 转换为字符串，可以避免 "'x' not supported between instances of 'float' and 'str'" 错误。
        b.append(str(x))
    else:
        pass

print(b)