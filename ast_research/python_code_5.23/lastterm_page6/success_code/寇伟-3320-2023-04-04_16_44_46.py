def judge_square(x,y):
    if x==y:
        print("It's a square")
    elif x!=y:
        print("It's a rectangle")
    elif x<0 or y<0:
        print("illegal data")
x,y=map(eval,input().split())
judge_square(x,y)
