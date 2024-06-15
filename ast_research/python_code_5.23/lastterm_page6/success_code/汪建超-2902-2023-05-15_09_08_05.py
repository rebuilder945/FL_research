n = int(input())
num1, num2 = 2, 1
sum = 0 # 初始化数列的前n项和
for i in range(n):
    sum += num1/num2
    # 更新数列的前两项
    num1, num2 = num1 + num2, num1
print("{:.4f}".format(sum))

