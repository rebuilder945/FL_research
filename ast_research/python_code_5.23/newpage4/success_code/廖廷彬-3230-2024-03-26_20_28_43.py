num_list=input().split()
num_list.sort(reverse=True)
res_str=".join(num_list)"
res_num=int(res_str)
print(res_str)
