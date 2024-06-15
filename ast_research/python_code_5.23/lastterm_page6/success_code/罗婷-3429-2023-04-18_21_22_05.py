s=input()   #直接使用input得到字符串
#print(s.isdigit())     #.isdigit()得到的结果为False或者True，s为字符串，如果字符串里面所有的元素都为数字，返回True，如果有不为数字的即False
digit_count=0
alpha_count=0
space_count=0
else_count=0
for i in s:
    if i.isdigit():
        digit_count+=1
    elif i.isalpha():
        alpha_count+=1
    elif i.isspace():
        space_count+=1
    else:
        else_count+=1
print(alpha_count,space_count,digit_count,else_count)
