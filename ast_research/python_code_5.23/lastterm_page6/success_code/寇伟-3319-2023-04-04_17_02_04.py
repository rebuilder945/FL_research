def judge(x,y):
    if x>=99 and y>=99:
        print("You won a scholarship of 500 yuan!")
    elif x<30 and y<30:
        print("You need to relearn!")
chinese=eval(input())
math = eval(input())
judge(chinese,math)
