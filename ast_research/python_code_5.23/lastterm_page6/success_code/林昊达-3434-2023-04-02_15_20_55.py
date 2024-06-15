# 【问题描述】

# 红色(red)、蓝色(blue)和黄色(yellow)被称为原色(primary color)。 当两种原色混合时，将得到次生色(secondary color)。

# 规则如下： 

# 当红色与蓝色混合时，将得到紫色(purple)。 

# 当红色与黄色混合时，将得到橙色(orange)。 

# 当蓝色与黄色混合时，将得到绿色(green)。 

# 编写一个程序，根据用户输入的欲混合的两种原色，输出混合得到的次生色的名称。 如果用户输入的不是三原色的名称，或者输入的两个颜色相同，则输出“error”

# 【输入形式】

# 原色1

# 原色2
# 【输出形式】

# 次生色 or error
# 【样例输入1】

# red

# blue

# 【样例输出1】

# purple

# 【样例输入2】

# red

# red

# 【样例输出2】

# error


primary_color=['red','blue','yellow']
secondary_color=['purple','orange','green']
color1=input()
color2=input()
if not color1 in primary_color and color2 in primary_color:
    print("error")
elif (color1,color2)==('red','blue'):
    print("purple")
elif (color1,color2)==('red','yellow'):
    print("orange")
elif (color1,color2)==('blue','yellow'):
    print("green")
else:
    print("error")

