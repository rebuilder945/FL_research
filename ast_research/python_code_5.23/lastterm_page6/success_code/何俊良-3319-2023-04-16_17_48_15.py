chinese_score = float(input().strip())  # 语文成绩
math_score = float(input().strip())     # 数学成绩

if chinese_score >= 99 and math_score >= 99:
    print("You won a scholarship of 500 yuan!")
elif chinese_score < 30 and math_score < 30:
    print("You need to relearn!")

