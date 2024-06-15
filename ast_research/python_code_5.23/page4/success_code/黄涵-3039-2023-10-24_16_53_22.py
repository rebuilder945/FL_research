#读入一个整数列表，输出删除最大元素和最小元素后的列表。最大元素和最小元素可能有多个
num = eval(input())
a = max(num)
b = min(num)
c = []
x = 0
while x<len(num) :
    if num[x] != a and num[x] != b:
        c.append(x)
        x += 1
print(num)
