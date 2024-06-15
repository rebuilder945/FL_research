math_grade = eval(input())
chinese_grade = eval(input())
if math_grade >= 99 and chinese_grade >= 99:
    print("You won a scholarship of 500 yuan!")
elif math_grade < 30 and chinese_grade < 30:
    print("You need to relearn!")
