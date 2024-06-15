num_list=[int(x)for x in input().split(',')]
sorted_nums=sorted(num_list,reverse=True)
max_num=int(''.join(map(str,sorted_nums)))
print(max_num)
