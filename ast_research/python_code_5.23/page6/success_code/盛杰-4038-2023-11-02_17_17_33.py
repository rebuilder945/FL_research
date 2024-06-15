s=input()
letter=0
space=0
digit=0
other=0
for i in s:
    if i.isalpha():
        letter+=1
    elif i.isspace():
        space+=1
    elif i.isdigit():
        digit+=1
    else:
        other+=1
print(letter,space,digit,other)
#输入一行字符（不能输入中文字符）
# 分别统计出该字符串英文字符、空格、数字和其他字符的个数#



