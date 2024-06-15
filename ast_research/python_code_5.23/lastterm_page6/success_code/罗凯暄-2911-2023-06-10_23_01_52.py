num = input("请输入要加密的数字：")
encrypted_num = ""
for i in range(len(num)):
    # 每位数字加上5，然后除以10得到的余数代替该数字
    new_num = (int(num[i]) + 5) % 10
    encrypted_num += str(new_num)
# 将第一位和最后一位交换，第二位与倒数第二位交换，依此类推
encrypted_num = encrypted_num[::-1]
print(encrypted_num)

