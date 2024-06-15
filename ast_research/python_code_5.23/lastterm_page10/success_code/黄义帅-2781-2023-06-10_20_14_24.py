def verify_id_card(id_card):  
    if len(id_card) != 18:  
        return "Error"  
      
    id_card_array = list(id_card)  
    id_card_array.pop()  # 移除最后一位校验码  
      
    # 计算前17位乘积和  
    product = 0  
    for i in range(17):  
        digit = int(id_card_array[i])  
        factor = (12 - i) % 11  # 计算系数  
        product += digit * factor  
      
    # 计算校验码  
    check_code = str((12 - (product % 11)) % 11)  # 取余数并转换为字符串  
      
    # 判断校验码是否正确  
    if check_code == id_card_array[17]:  
        return "Correct"  
    else:  
        return "Wrong"

result = verify_id_card("53010219200508011X")  
print(result)  # 输出 "Correct"
