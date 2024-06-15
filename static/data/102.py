n=input()
a=""
for x in n:
    x=(int(x)+5)%10
    a+=str(x)
a=list(a)
a.reverse()
b=""
for x in a:
    b += str(x) # 将 x 转换为字符串后再追加到 b 中
    #尝试将一个列表 a 连接到字符串 b 中，这是不允许的，
    #应该将列表中的元素转换为字符串后再连接到 b 中。
print(b)
print(type(a))


