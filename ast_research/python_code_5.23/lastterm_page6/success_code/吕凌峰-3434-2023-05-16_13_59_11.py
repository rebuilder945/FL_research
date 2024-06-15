# 颜色混合器
# 【问题描述】
# 红色(red)、蓝色(blue)和黄色(yellow)被称为原色(primary color)。
# 当两种原色混合时，将得到次生色(secondary color)。
# 规则如下： 
# 当红色与蓝色混合时，将得到紫色(purple)。 
# 当红色与黄色混合时，将得到橙色(orange)。 
# 当蓝色与黄色混合时，将得到绿色(green)。 
# 编写一个程序，根据用户输入的欲混合的两种原色，输出混合得到的次生色的名称。
# 如果用户输入的不是三原色的名称，或者输入的两个颜色相同，则输出“error”
def colour_mix(x, y):
    if x == 'red' or y == 'red':
        if x == 'yellow' or y == 'yellow':
            return 'orange'
        if x == 'blue' or y == 'blue':
            return 'purple'
        else:
            return 'error'
    elif x == 'yellow' or y == 'yellow':
        if x == 'red' or y == 'red':
            return 'orange'
        if x == 'blue' or y == 'blue':
            return 'green'
        else:
            return 'error'
    elif x == 'blue' or y == 'blue':
        if x == 'red' or y == 'red':
            return 'purple'
        if x == 'yellow' or y == 'yellow':
            return 'green'
        else:
            return 'error'
    else:
        return 'error'
colour1 = input()
colour2 = input()
print(colour_mix(colour1, colour2))
