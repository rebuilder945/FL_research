length = float(input().strip())  # 方形长度
width = float(input().strip())   # 方形宽度

if width <= 0 or length <= 0:
    print("illegal data")
elif length == width:
    print("It's a square")
else:
    print("It's a rectangle")

