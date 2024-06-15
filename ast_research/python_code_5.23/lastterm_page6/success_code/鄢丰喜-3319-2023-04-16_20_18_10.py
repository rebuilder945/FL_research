a = int(input("请输入数学成绩："))
b = int(input("请输入语文成绩："))
if a >= 0 and a <= 100 and b >= 0 and b <= 100:
    if a > 99 and b > 99:
        print("You won a scholarship of 500 yuan!")
    elif a < 30 and b < 30:
        print("You need to relearn!")
