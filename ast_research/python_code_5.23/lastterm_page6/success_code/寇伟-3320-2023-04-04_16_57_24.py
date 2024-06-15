def judge_square(x,y):
    if x==y and (x>0 and y>0):
        print("It's a square")
    elif x!=y and (x>0 and y>0):
        print("It's a rectangle")
    else:
        print("illegal data")
x=eval(input())
y=eval(input())
judge_square(x,y)
