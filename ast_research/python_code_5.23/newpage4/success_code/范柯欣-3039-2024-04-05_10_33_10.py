def remove_extremes(input_list):
    if not input_list:
        return []
    
    min_val = min(input_list)
    max_val = max(input_list)
    
    for _ in range(input_list.count(min_val)):
        input_list.remove(min_val)
        
    for _ in range(input_list.count(max_val)):
        input_list.remove(max_val)
    
    return input_list

# 读取输入列表
input_str = input("请输入整数列表（包括方括号）：")
input_list = eval(input_str)

# 调用函数删除最大值和最小值后输出结果
result = remove_extremes(input_list)
print(result)
