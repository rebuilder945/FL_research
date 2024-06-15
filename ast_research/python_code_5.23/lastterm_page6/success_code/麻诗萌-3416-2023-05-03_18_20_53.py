money=input()
if money[0] in ["&"] :
    dollar=eval(money[1:])/6.78
    kind="$"   
    print("%s%.2f"%(kind,dollar))
elif money[0] in ["$"] :
    yuan=eval(money[1:])*6.78
    kind="&"
    print("%s%.2f"%(kind,yuan))
elif money[0:3] in ["RMB"] :
    dollar=eval(money[3:])/6.78
    kind="USD"   
    print("%s%.2f"%(kind,dollar))
elif money[0:3] in ["USD"] :
    yuan=eval(money[3:])*6.78
    kind="RMB"
    print("%s%.2f"%(kind,yuan))
else:
    print("Error")
