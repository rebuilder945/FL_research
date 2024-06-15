def max_integer(lst):
    sorted_lst=sorted(lst,reverse=Ture)
    num_str=num_str.lstrip('0')
    if not num_str:
        return 0
    max_num=int(num_str)
    return max_num
input_list=input()
print(max_integer(input_list))
