num_list = eval(input())
num_list.sort(reverse=True)
str_list=[]
for x in num_list:
    str_list.append(str(x))
str_result="".join(str_list)
print(str_result)
