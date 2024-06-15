s=input()
if s[0] in ["$"]:
    a=eval(s[1,-1])*6.78
    print("&""%.2f"%(a))
elif s[0] in ["&"]:
    a=eval(s[1,-1])/6.78
    print("$""%.2f"%(a))
elif s[0,3] in ["RMB"]:
    a=eval(s[3,-1])/6.78
    print("USD""%.2f"%(a))
elif s[0,3] in ["USD"]:
    a=eval(s[3,-1])*6.78
    print("USD""%.2f"%(a))
else:
    print("Error")

