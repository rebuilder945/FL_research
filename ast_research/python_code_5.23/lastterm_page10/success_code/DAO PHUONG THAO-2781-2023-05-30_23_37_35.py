def validate_id_card(id_card):
    # 判断身份证校验码是否正确
    if len(id_card) != 18:
        return "Error"  # 不是18位身份证号码，返回错误

    # 定义校验码映射表
    check_map = {
        0: '1', 1: '0', 2: 'X', 3: '9', 4: '8', 5: '7', 6: '6', 7: '5', 8: '4', 9: '3', 10: '2'
    }

    # 获取前17位数字和系数
    factors = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    digits = list(id_card[:17])

    # 计算乘积和
    total = sum([int(d) * f for d, f in zip(digits, factors)])

    # 计算校验码对应的余数
    remainder = total % 11

    # 判断校验码是否正确
    if check_map[remainder] == id_card[-1]:
        return "Correct"  # 校验码正确
    else:
        return "Wrong"  # 校验码错误


# 读取输入的身份证号码
id_card = input()

# 验证身份证校验码并输出结果
result = validate_id_card(id_card)
print(result)



