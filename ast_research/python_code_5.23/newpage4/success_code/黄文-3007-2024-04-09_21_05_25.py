# 使用ast.literal_eval()来安全地解析输入的字符串
lst = ast.literal_eval(input())

# 假设n和m是输入的n和m的值
n, m = map(int, input().split(','))

# 检查n和m是否在列表lst的范围内
if n < 0 or m >= len(lst) or n > m:
    print("error")
else:
    # 生成新的列表，删除n到m之间的元素
    result_list = lst[:n] + lst[m+1:]
    print(result_list)

       
