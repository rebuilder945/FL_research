#【问题描述】
#读入一个自然数构成的列表，找出其中的每一个素数，然后放入另外一个列表，并输出这个列表。
#【输入形式】
#按照列表的形式输入，包括方括号，元素之间用逗号分隔。
#【输出形式】
#直接用print输出列表
lst1 = eval(input())
lst2 = []
for x in lst1: 
    for i in range(2,x):
        if (x%i) == 0:
            break
    if i == x-1:
        lst2.append(x)
    
        
