# 2023-2024（2）基础题库练习：第4章
# 第一题
# lst=eval(input())
# lst.sort(reverse=True)
# sum=''
# for i in range(len(lst)):
#     sum+=str(lst[i])
# print(int(sum))

# 第二题
input_list = list(map(int, input("请输入一个自然数列表，用空格分隔每个数字: ").split()))
count_dict = {}
for num in input_list:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

# 查找只出现一次的元素
unique_elements = [num for num in count_dict if count_dict[num] == 1]

# 如果没有只出现一次的元素，则输出False
if not unique_elements:
    print(False)
else:
    # 将唯一元素升序输出
    unique_elements.sort()
    print(unique_elements)

        
