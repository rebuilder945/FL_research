jiazhi=input()
if jiazhi[0] in ["$"]:
    jiazhi=float(jiazhi[1:])
    jieguo = jiazhi*6.78
    print("&"+"%.2f"%jieguo)
elif jiazhi[0] in ["&"]:
    jiazhi=float(jiazhi[1:])
    jieguo = jiazhi/6.78
    print("$"+"%.2f"%jieguo)
elif jiazhi[0] in ["R"]:
    jiazhi=float(jiazhi[3:])
    jieguo = jiazhi/6.78
    print("USD"+"%.2f"%jieguo)
elif jiazhi[0] in ["U"]:
    jiazhi=float(jiazhi[3:])
    jieguo = jiazhi*6.78
    print("RMB"+"%.2f"%jieguo)
else:
    print("Error")
