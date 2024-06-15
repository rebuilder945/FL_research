money=(input())
if money[0] in ["R"]:
    worth=(eval(money[3:]))/6.78
    print("%s""%.2f"%("USD",worth))
elif money[0] in ["&"]:
    worth=(eval(money[1:]))/6.78
    print("%s""%.2f"%("$",worth))
elif money[0] in ["$"]:
    worth=(eval(money[1:]))*6.78
    print("%s""%.2f"%("&",worth))
elif money[0] in ["U"]:
    worth=(eval(money[3:]))*6.78
    print("%s""%.2f"%("RMB",worth))
else:
    print("Error")

