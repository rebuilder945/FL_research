from collections import Counter

# 读取输入的自然数列表
input_list = eval(input())

# 使用Counter统计列表中每个元素出现的次数
counter = Counter(input_list)

# 找出只出现一次的元素并按升序输出
unique_elements = [num for num, count in counter.items() if count == 1]
if unique_elements:
    sorted_unique_elements = sorted(unique_elements)
    output = ','.join(map(str, sorted_unique_elements))
    print(output)
else:
    print(False)

