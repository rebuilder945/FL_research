#三种原色，如果不在原色之中就报错，如果颜色一样就报错。红蓝得紫，红黄得橙，蓝黄得绿
color1= input() 
color2 = input()
if color1 == color2:
    print("error")
elif color1 not in ["red","yellow","blue"] or color2 not in ["red","yellow","blue"]:
    print("error")
elif color1 in ["red","blue"] and color2 in ["red","blue"] :
    print("purple")
elif color1 in ["red","yellow"] and color2 in ["red","yellow"] :        # color1 and color2 in ["red","yellow"] 不可以！
    print("orange")
else:
    print("green")
#简化：因为这里颜色不要求顺序，所以想用集合
#s1 = {color1,color2}
#purpleset = {"red","blue"}
#if si == purpleset

