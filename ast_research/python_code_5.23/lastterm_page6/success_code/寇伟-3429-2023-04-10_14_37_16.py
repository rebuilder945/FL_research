s=input('请输入内容：')
letter=0
space=0
digit=0
other=0
for i in s:
    if i.isalpha():#判断是否是字母
        letter+=1
    elif i.isspace():#判断是否是空格
        space+=1
    elif i.isdigit():#判断是否是数字
        digit+=1
    else:
        other+=1
print(letter,space,digit,other)







