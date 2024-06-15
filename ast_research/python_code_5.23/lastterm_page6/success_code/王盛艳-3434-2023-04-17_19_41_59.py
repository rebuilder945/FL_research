color = {"red":1,"blue":2,"yellow":3}
color1 = input()
color2 = input()
mix = color.get(color1,10) + color.get(color2,10)
if mix == 3:
    print("purple")
elif mix == 4:
    print("orange")
elif mix == 5:
    print("green")
else:
    print("error")
