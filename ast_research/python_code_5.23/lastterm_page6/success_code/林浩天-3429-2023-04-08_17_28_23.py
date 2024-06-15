s=input()
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
#————————————————
#版权声明：本文为CSDN博主「谭你一个脑瓜崩」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
#原文链接：https://blog.csdn.net/qq_54226199/article/details/127326303
