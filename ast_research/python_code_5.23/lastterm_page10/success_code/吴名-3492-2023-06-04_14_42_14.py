def find_first_unique_char(string):
    if len(string) == 0:
        return "None"
    else:
        char_count = {}
        for char in string:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        for char in string:
            if char_count[char] == 1:
                return char

# 从标准输入获取字符串
input_string = input()

# 调用函数并输出结果
result = find_first_unique_char(input_string)
print(result)


