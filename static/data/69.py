ls = list(map(str, input().split(',')))
#使用 map() 函数时，提供的参数数量不足。
#使用 map(str, input().split(',')) 来将逗号分隔的输入转换为字符串类型，并将其放入列表中。
n, m = eval(input())
a = []

if n < len(ls):
    a.append(ls[n])
    a = a * m
    del ls[n]
    print(ls + a)
else:
    print("error")