# 评奖系统
# 【问题描述】
# 编程实现学校评奖系统
# （1）如果数学成绩大于等于99并且语文成绩大于等于99，获奖学金500。
# （2）如果数学和语文成绩都小于30，输出重修。

def reward(Chinese, Maths):
    if Chinese >= 99 and Maths >= 99:
        return 'You won a scholarship of 500 yuan!'
    elif Chinese < 30 and Maths < 30:
        return 'You need to relearn!'
    else:
        return ''
x = eval(input())
y = eval(input())
print(reward(x, y))
