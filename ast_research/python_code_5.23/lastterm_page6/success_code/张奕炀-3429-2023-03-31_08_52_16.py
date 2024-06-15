s = input()
letters = 0
space = 0
digit = 0
others = 0
for i in s:
    if i.isalpha():
        letters = letters + 1
    elif i.isspace():
        space = space + 1
    elif i.isdigit():
        digit = digit + 1
    else:
        others = others + 1
print(letters,end=" ")
print(space,end=" ")
print(digit,end=" ")
print(others,end=" ")


#isalphe() 判断字符串中是否全部为字母
#isspace() 判断字符串中是否全部为空格
#isdigit() 判断字符串中是否全部为数字
