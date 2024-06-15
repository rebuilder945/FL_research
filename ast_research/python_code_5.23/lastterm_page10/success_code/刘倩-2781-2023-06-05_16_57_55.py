id_number = input()  # 输入一个18位身份证号码

if len(id_number) != 18:  # 判断输入是否为18位
    print("Error")  # 如果不是18位，输出 "Error"
else:
    coefficients = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 系数列表
    check_code_mapping = {0: 1, 1: 0, 2: "X", 3: 9, 4: 8, 5: 7, 6: 6, 7: 5, 8: 4, 9: 3, 10: 2}  # 校验码映射表

    sum_product = 0  # 乘积求和
    for i in range(17):
        digit = int(id_number[i])  # 提取身份证号码的每一位数字
        coefficient = coefficients[i]  # 对应位的系数
        sum_product += digit * coefficient  # 乘积求和

    remainder = sum_product % 11  # 求和取余数

    if check_code_mapping[remainder] == id_number[-1]:  # 判断校验码是否正确
        print("Correct")  # 如果校验码正确，输出 "Correct"
    else:
        print("Wrong")  # 如果校验码错误，输出 "Wrong"

