#红色(red)、蓝色(blue)和黄色(yellow)被称为原色(primary color)。 
#当两种原色混合时，将得到次生色(secondary color)。
#规则如下：
#当红色与蓝色混合时，将得到紫色(purple)。 
#当红色与黄色混合时，将得到橙色(orange)。 
#当蓝色与黄色混合时，将得到绿色(green)。 
#编写一个程序，根据用户输入的欲混合的两种原色，输出混合得到的次生色的名称。
#如果用户输入的不是三原色的名称，或者输入的两个颜色相同，则输出“error”
pc=['red','blue','yellow']
c1=input()
c2=input()
cset1=['red','blue']
cset2=['red','yellow']
cset3=['blue','yellow']
if c1 not in pc or c2 not in pc or c1==c2:
    print('error')
elif c1 in cset1 and c2 in cset1:
    print("purple")
elif c1 in cset2 and c2 in cset2:
    print("orange")
elif c1 in cset3 and c2 in cset3:
    print("green")
