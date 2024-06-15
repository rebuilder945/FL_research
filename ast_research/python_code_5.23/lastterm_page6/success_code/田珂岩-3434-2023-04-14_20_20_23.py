color1 = input()
color2 = input()
# 用集合保存数据 集合具有确定性互异性【无序性】
s1 = {color1,color2}
purpleset = {"red","blue"}
orangeset = {"red","yellow"}
greenset = {"blue","yellow"}
tricolor = {"red","blue","yellow"}
if (color1 not in tricolor) or (color2 not in tricolor) or color1 == color2:
    print("error")
elif s1 == purpleset:
    print("purple")
elif s1 == orangeset:
    print("orange")
else:
    print("green")             

