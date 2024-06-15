def square(length,width):
    if length == width:
        print("It's a square")
    elif length != width:
        print("It's a rectangle")
    else:
        print("illegal data") 
length = eval(input())
width = eval(input())
square(length,width)

