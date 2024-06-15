ls1 = eval(input())

# 将 True 值转换为字符串
for i in range(len(ls1)):
    if ls1[i] == True and type(ls1[i]) == bool:
        ls1[i] = str(ls1[i])

ls2 = ls1.copy()
i = 0
while i < len(ls2):
    if ls1.count(ls2[i]) != 1:
        ls1.remove(ls2[i])
        i = 0
    else:
        i += 1
#出现问题的原因是，在遍历 ls1 列表的同时修改了它，这可能导致迭代和修改冲突。
#将第二个循环改为使用 while 循环，并在删除元素后将索引 i 重置为0，以确保能够正确地删除重复元素。
for i in range(len(ls1)):
    if ls1[i] == 'True':
        ls1[i] = eval(ls1[i])

print(ls1)