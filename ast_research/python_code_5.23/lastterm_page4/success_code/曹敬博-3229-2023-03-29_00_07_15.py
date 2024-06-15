num_list = eval(input()) 
count_dict = {} 
for num in num_list:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1
result_list = [] 
for num, count in count_dict.items():
    if count == 1:
        result_list.append(num)
if result_list:
    result_list.sort() # 排序
    print(','.join(str(num) for num in result_list)) 
else:
    print(False) 
