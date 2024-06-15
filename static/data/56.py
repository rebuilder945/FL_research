a = list(input())
b = input()
i = 0
c = []

for i in range(min(len(a), len(b))):
    c.append([a[i], b[i]])
    #使用append将a,b逐个字符组合成新的列表c
    print(c, end='')
    #print([c],end=()) 中的 end=() 会导致错误，因为 end 参数需要是一个字符串，而不是一个空的元组。

if c:
    del c[-1]
    print(c)
    #prin(c) 应该是 print(c)，并且在 del c[-1] 之前应该检查 c 是否为空。