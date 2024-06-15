# 获取用户输入的语文和数学成绩
chinese_score = int(input())
math_score = int(input())

# 判断是否获得奖学金
if chinese_score >= 99 and math_score >= 99:
    print("You won a scholarship of 500 yuan!")
# 判断是否需要重修
elif chinese_score < 30 and math_score < 30:
    print("You need to relearn!")

