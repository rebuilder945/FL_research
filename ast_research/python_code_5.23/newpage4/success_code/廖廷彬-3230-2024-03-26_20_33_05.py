num_list=input().strip('[]').split(',')
num_list=[int(num)for num in num_list]
sorted_nums=sorted(num_list, reverse=True)
max_num=int(''.join(map(str,sorted_nums)))
print(max_num)
