input_list=eval(input())
max_s=max(input_list)
min_s=min(input_list)
result_list=[x for x in input_list if x!=max_s and x!=min_s]
print(result_list)

