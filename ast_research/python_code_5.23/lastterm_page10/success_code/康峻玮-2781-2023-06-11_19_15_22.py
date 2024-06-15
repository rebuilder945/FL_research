id_num = input()

# 检验输入是否为 18 位身份证号
if len(id_num) != 18:
    print("Error")
else:
    # 系数列表
    coefficients = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    
    # 校验码对应的字典
    check_code_dict = {
        0: "1",
        1: "0",
        2: "X",
        3: "9",
        4: "8",
        5: "7",
        6: "6",
        7: "5",
        8: "4",
        9: "3",
        10: "2"
    }
    
    # 计算前 17 位数字和系数的积
    sum_product = sum([int(id_num[i]) * coefficients[i] for i in range(17)])
    
    # 计算余数并查找对应的校验码
    check_code = check_code_dict[(12 - (sum_product % 11)) % 11]
    
    # 判断校验码是否正确
    if check_code == id_num[-1]:
        print("Correct")
    else:
        print("Wrong")
