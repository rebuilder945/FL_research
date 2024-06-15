def award_system():
    chinese_score = int(input("请输入语文成绩："))
    math_score = int(input("请输入数学成绩："))
    if chinese_score >= 99 and math_score >= 99:
        return "You won a scholarship of 500 yuan!"
    elif chinese_score < 30 and math_score < 30:
        return "You need to relearn!"
    else:
        return "Sorry, you are not eligible for any awards."
print(award_system())


