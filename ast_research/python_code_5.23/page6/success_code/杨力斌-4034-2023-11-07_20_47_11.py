color1 = input()
color2 = input()
sl = {color1,color2}
tricolor = {"red","blue","yellow"}
purplelist = {"red","blue"}
orangelist = {"red","yellow"}
grenelist = {"blue","yellow"}
if color1 not in tricolor or color2 not in tricolor or color1 == color2:
    print("error")
elif sl == purplelist:
    print("purple")
elif sl == orangelist:
    print("orange")
else:
    print("green")
