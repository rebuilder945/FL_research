# 【问题描述】

# 输入一行字符（不能输入中文字符），分别统计出该字符串英文字符、空格、数字和其他字符的个数

# 【输入形式】

# 字符串

# 【输出形式】

# 英文字符个数 空格个数 数字字符个数 其他字符个数

# 【样例输入】

# abcd 1 2 3 4!@#$$%^

# 【样例输出】

# 4 4 4 7

# 【样例说明】

# 输出数字之间用空格隔开

s=input()
ls=list(s)
ls.sort()
eng=0
space=0
num=0
other=0
for i in ls:
    if i.isdigit():     #也可使用type(i)==int
        num+=1
    elif i.isspace():   #也可使用type(i)==" "
        space+=1
    elif i.isalpha():   #也可使用type(i)==str，对于空格不会重复计算
        eng+=1
    else:
        other+=1
print(eng,space,num,other)
