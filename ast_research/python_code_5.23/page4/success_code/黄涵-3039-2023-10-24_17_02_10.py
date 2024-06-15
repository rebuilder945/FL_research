#读入一个整数列表，输出删除最大元素和最小元素后的列表。最大元素和最小元素可能有多个
num = eval(input())
a = max(num)
b = min(num)
c = []
for x in num :
    if x != a and x != b:
        c.append(x)
print(c)
