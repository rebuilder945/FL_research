#【问题描述】
#读入一个自然数构成的列表，找出其中的每一个素数，然后放入另外一个列表，并输出这个列表。
#【输入形式】
#按照列表的形式输入，包括方括号，元素之间用逗号分隔。
#【输出形式】
#直接用print输出列表
#【样例输入】
#[2,3,5,7,9,11,23]
#【样例输出】
#[2, 3, 5, 7, 11, 23]
#【样例说明】
#所有的输入数据在一行。所有的输出在一行。
#【评分标准】
#通过所有测试数据
def sushu(x):
    if x >=2 and type(x) ==int:
        for i in range(2,x//2):
            if x%i ==0:
                return False
        return True
    else:
        return False


lst1=eval(input())
lst2 = []
for x in lst1:
    if sushu(x):
        lst2.append(x)
print(lst2)


              



