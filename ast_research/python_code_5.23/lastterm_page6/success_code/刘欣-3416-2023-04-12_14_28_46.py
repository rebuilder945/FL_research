jiazhi=eval(input())
if jiazhi[0] in ["$"]:
    jieguo = jiazhi/6.78
    print("&"+"%.2f"%jieguo)
elif jiazhi[0] in ["&"]:
    jieguo = jiazhi*6.78
    print("$"+"%.2f"%jieguo)
elif jiazhi[0] in ["R"]:
    jieguo = jiazhi*6.78
    print("USD"+"%.2f"%jieguo)
elif jiazhi[0] in ["U"]:
    jieguo = jiazhi/6.78
    print("RMB"+"%.2f"%jieguo)
else:
    print("Error")
