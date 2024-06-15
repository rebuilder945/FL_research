#编程实现学校评奖系统，（1）如果数学成绩大于等于99并且语文成绩大于等于99，获奖学金500。
#（2）如果数学和语文成绩都小于30，输出重修。
a = eval(input())
b = eval(input())
if a >= 99 and b >= 99 :
    print("You won a scholarship of 500 yuan!")
elif a < 30 and b < 30 :
    print("You need to relearn!")
