"""输入一行字符（不能输入中文字符），分别统计出该字符串英文字符、空格、数字和其他字符的个数
【输入形式】
字符串
【输出形式】
英文字符个数 空格个数 数字字符个数 其他字符个数
【样例输入】
abcd 1 2 3 4!@#$$%^
【样例输出】
4 4 4 7"""
a = input()
alpha,digit,space,other=0,0,0,0
for i in a :
    if i.isalpha():
        alpha+=1
    elif i.isdigit():
        digit+=1
    elif i.isspace():
        space+=1
    else:other+=1
print(alpha,space,digit,other,sep=" ")
