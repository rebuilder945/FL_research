def largest_number(num_list):
    num_list=sorted(map(str,num_list),key=lambda x:x*3,reverse=True)
    return''.join(num_list)
nums=input()
largest_num=largest_number(nums)
print(largest_num)
