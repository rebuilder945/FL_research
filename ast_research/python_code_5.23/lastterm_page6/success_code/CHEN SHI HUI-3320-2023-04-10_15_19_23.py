from turtle import width


len=eval(input())
width=eval(input())
if len==width and(len>0 and width>0):
    print("It's a square")
elif len!=width and(len>0 and width>0):
    print("It's a rectangle")
elif len<=0 or width<=0:
    print("illegal data")
