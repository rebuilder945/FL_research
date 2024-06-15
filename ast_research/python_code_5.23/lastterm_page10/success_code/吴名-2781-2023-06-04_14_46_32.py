def validate_id(id_number):
    # 验证身份证号码长度是否为18位
    if len(id_number) != 18:
        return "Error"
    
    # 获取前17位数字和校验码
    digits = id_number[:-1]
    check_code = id_number[-1]
    
    # 定义系数和校验码映射关系
    coefficients = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    check_map = {0: "1", 1: "0", 2: "X", 3: "9", 4: "8", 5: "7", 6: "6", 7: "5", 8: "4", 9: "3", 10: "2"}
    
    # 计算乘积和
    total = sum(int(digits[i]) * coefficients[i] for i in range(17))
    
    # 计算余数
    remainder = total % 11
    
    # 判断校验码是否正确
    if check_map[remainder] == check_code:
        return "Correct"
    else:
        return "Wrong"

# 从标准输入获取身份证号码
id_number = input()

# 验证校验码并输出结果
result = validate_id(id_number)
print(result)

