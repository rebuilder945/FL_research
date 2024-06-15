dummy = eval(input())
for x in dummy[:]: #建立了一个原列表的copy,然后每个都遍历了,所以可以remove多个
    while dummy.count(x) > 1:
        dummy.remove(x)
print(dummy)

