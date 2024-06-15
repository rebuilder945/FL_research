def max_number_from_list(lst):
    lst.sort(reverse=True)
    result = ''.join(map(str, lst))
    return int(result)
input_list = eval(input("请输入包含正整数的列表，每个正整数只有一位，格式如[1, 2, 3, 4]: "))
result = max_number_from_list(input_list)
print(result)
