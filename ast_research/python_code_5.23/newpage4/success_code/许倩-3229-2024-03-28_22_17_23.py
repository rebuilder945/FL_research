# 2023-2024（2）基础题库练习：第4章
# 第一题
# lst=eval(input())
# lst.sort(reverse=True)
# sum=''
# for i in range(len(lst)):
#     sum+=str(lst[i])
# print(int(sum))

# 第二题
def find_unique_element(lst):
    # 使用集合来计算每个元素出现的次数
    count_dict = {num: lst.count(num) for num in set(lst)}
    
    # 找出只出现一次的元素
    unique_elements = [num for num, count in count_dict.items() if count == 1]
    
    # 如果找到了只出现一次的元素，就进行排序并返回
    if unique_elements:
        return sorted(unique_elements)
    else:
        return False

# 测试
lst = [1, 2, 3, 2, 4, 5, 5, 6, 6, 6]
print(find_unique_element(lst))  # 输出: [1, 3, 4]

lst2 = [1, 1, 2, 2, 3, 3]
print(find_unique_element(lst2))  # 输出: False


        
