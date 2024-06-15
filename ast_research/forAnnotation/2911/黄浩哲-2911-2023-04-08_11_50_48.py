num = input("请输入要加密的数字：")

# 加密过程
result = ""
for i in range(len(num)):
    digit = (int(num[i]) + 5) % 10
    result += str(digit)

# 交换数字
result = list(result)
for i in range(len(result) // 2):
    result[i], result[-i-1] = result[-i-1], result[i]
result = "".join(result)

print("加密后的数字密码为：" + result)

