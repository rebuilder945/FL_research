import re

# 定义转译字符
escape_chars = ['\\\\', '\\\'', '\\"', '\\b', '\\f', '\\n', '\\r', '\\t', '\\v', '\a']

def is_safe_nested_list(nested_list_str):
    # 判断字符串是否符合嵌套列表规范格式：只包含数字、逗号、方括号和空格
    if not re.match(r'^[\d,\[\]\s]+$', nested_list_str):
        return False
    # 转义特殊字符
    for ec in escape_chars:
        nested_list_str = nested_list_str.replace(ec, '')
    # 将括号内内容替换为空格，再根据空格分割成单个字符列表
    chars = re.sub(r'(\[[^\[\]]*\])', ' ', nested_list_str).split()
    # 检查每个字符是否符合数字格式
    for c in chars:
        if  not re.match(r'^\d+$',c):
            return False
    return True

def count_element(nested_list, level):
    if level == 1:  # 搜索到指定的层次
        return len(nested_list)
    element_count = 0
    for item in nested_list:
        if isinstance(item, list):  # 如果遇到列表，继续递归向下搜索
            element_count += 1  # 嵌套列表算一个元素
        elif level > 2:  # 当前不是最后一层时，还需进一步递归搜索下一层
            inner_level = level - 1
            if isinstance(item, tuple):  # 元组类型也需转换成列表类型
                item = list(item)
            if isinstance(item, list):
                element_count += count_element(item, inner_level)
        else:  # 已到达最后一层
            element_count += 1
    return element_count

nested_list_str = input().strip()
level = int(input().strip())
if is_safe_nested_list(nested_list_str):
    nested_list = eval(nested_list_str)  # 将输入字符串转换成嵌套列表
    count = count_element(nested_list, level)
    print(count)
else:
    print("非法输入！")
