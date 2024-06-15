num = input("请输入要加密的数字：")
encrypted_num = ""
for i in range(len(num)):
    # 将每个数字加上5，然后对10取余数
    new_digit = (int(num[i]) + 5) % 10
    encrypted_num += str(new_digit)

# 将第一位和最后一位交换，第二位和倒数第二位交换，以此类推
encrypted_num = list(encrypted_num)
for i in range(len(encrypted_num) // 2):
    encrypted_num[i], encrypted_num[-i-1] = encrypted_num[-i-1], encrypted_num[i]
    
encrypted_num = "".join(encrypted_num)

print(encrypted_num)
