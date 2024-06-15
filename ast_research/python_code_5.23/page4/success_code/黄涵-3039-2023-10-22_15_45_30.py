#读入一个整数列表，输出删除最大元素和最小元素后的列表。最大元素和最小元素可能有多个
num = eval(input())
a = max(num)
b = min(num)
for i in num :
    if i == a:
        num.remove(i)
for x in num :
    if x == b:
        num.remove(b)
print(num)

