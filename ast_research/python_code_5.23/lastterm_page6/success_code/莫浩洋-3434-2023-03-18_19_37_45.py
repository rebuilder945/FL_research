'''当红色与蓝色混合时，将得到紫色(purple)。 
当红色与黄色混合时，将得到橙色(orange)。 
当蓝色与黄色混合时，将得到绿色(green)。 
编写一个程序，根据用户输入的欲混合的两种原色，输出混合得到的次生色的名称。 如果用户输入的不是三原色的名称，或者输入的两个颜色相同，则输出“error”
【输入形式】
原色1
原色2
【输出形式】
次生色 or error'''
ocl=['红色','蓝色','黄色']
p=['红色','蓝色']
o=['红色','黄色']
g=['蓝色','黄色']
a=input()
b=input()
if (not a in ocl) or (not b in ocl) or a==b:
    print("error")
else:
    if a in p and b in p:
        print("紫色")
    if a in o and b in o:
        print("橙色")
    if a in g and b in g:
        print("绿色")
