#字符统计
#输入一行字符（不能输入中文字符），分别统计出该字符串英文字符、空格、数字和其他字符的个数
def CountString(x):
    letter = 0
    space = 0
    nums = 0
    others = 0
    for i in x:
        Ascii = ord(i)
        if Ascii >= 97 and Ascii <= 122:    #小写英文字母ASCII码范围
            letter += 1
        elif Ascii >= 65 and Ascii <=90:    #大写英文字母ASCII码范围
            letter += 1
        elif Ascii >= 48 and Ascii <= 57:   #数字0-9字母ASCII码范围
            nums += 1
        elif Ascii == 32:                   #空格' ' ASCII码
            space += 1
        else:
            others += 1
    return '%s %s %s %s'%(letter, space, nums, others)
Str = list(input())
print(CountString(Str))
