import re
input_str=eval(input())
num_list=re.findall("\d+",input_str)
max_len=0
max_len_num=""
for num in num_list:
      if len(num) >= max_len:
          max_len_num=num
          max_len=len(num)
if max_len_num=="":
    print("no digit")
else:
    print(max_len_num)
