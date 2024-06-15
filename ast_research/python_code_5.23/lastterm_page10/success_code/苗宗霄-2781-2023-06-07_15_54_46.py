id_card = input()  # 获取输入的身份证号码

if len(id_card) != 18:  # 判断输入是否为18位
    print("Error")
else:
    factors = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 每一位的系数
    check_codes = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']  # 校验码对应表

    total = 0
    for i in range(17):
        total += int(id_card[i]) * factors[i]  # 计算前17位的乘积和

    remainder = total % 11  # 计算余数 
    check_code = check_codes[remainder]  # 获取对应的校验码

    if check_code == id_card[-1]:  # 判断校验码是否正确
        print("Correct")
    else:
        print("Wrong")

