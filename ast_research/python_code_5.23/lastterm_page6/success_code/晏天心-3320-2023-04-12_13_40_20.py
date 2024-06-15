length = eval(input())
width = eval(input())
if length <= 0 or width <= 0:
    print("illegal data")
else:
    if length == width:
        print("It's a square")
    else:
        print("It's a rectangle")
# if length > 0 and width > 0 and length == width:
#     print("It's a square")
# elif length > 0 and width > 0 and length != width:
#     print("It's a rectangle")
# elif length < 0 or width < 0:
#     print("illegal data")

