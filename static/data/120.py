a = eval(input("请输入一个整数："))
d = []
for y in range(a):
    if str(y)[0] == str(y)[-1]:
        d.append(y)

b = []
for i in d:
    c = True
    for x in range(2, i):
        if i % x == 0:
            c = False
            break
    if c and i != 0 and i != 1:
        b.append(i)

for num in b:
    print(num, end='')
#在 range(b) 中，b 是一个列表，而 range() 函数需要一个整数作为参数，而不是一个列表。