'''
读入一个自然数构成的列表，找出其中的每一个素数，然后放入另外一个列表，并输出这个列表。
按照列表的形式输入，包括方括号，元素之间用逗号分隔。
直接用print输出列表
[2,3,5,7,9,11,23]
【样例输出】
[2, 3, 5, 7, 11, 23]
【样例说明】
所有的输入数据在一行。所有的输出在一行。
'''
a=eval(input())
b=[]

for i in a:
   if i <=1 :
        b.append(i)
   else:
        for x in range(2,i):
            if i%x==0:
                b.append(i)
                break
c=list(set(a)-set(b))  
c.sort()
print(c)
