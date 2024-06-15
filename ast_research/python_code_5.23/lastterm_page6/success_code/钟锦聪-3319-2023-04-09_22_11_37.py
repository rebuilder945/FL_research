# （1）如果数学和语文成绩都大于等于99，输出:You won a scholarship of 500 yuan!

# （2）如果数学和语文成绩都小于30，输出:You need to relearn!
a = eval(input())
b = eval(input())
if a >=99 and b >= 99:
    print("You won a scholarship of 500 yuan!")
elif a<30 and b<30:
    print("You need to relearn!")
