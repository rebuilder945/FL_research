def square(length,width):
    if length <0 or width < 0 :
        print("illegal data")
    elif length == width:
        print("It's a square")
    elif length != width:
        print("It's a rectangle")

length = eval(input())
width = eval(input())
square(length,width)

