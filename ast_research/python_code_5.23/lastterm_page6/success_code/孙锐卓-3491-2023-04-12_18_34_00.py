def shift(lst):

    if not input_list:
        return input_list
    last_elem = input_list[-1]
    for i in range(len(input_list)-1, 0, -1):
        input_list[i] = input_list[i-1]
    input_list[0] = last_elem
    return input_list

input_list = input().split(',')
print(shift_list(input_list))


list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

