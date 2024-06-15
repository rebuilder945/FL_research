Money = input()
if Money[0] == "&":
    M = (eval(Money[1:])) / 6.78
    print("$""%.2f"%(M))
elif Money[0] == "$":
    M = (eval(Money[1:]))* 6.78
    print("&""%.2f"%(M))
elif Money[0:3] == "RMB":
    M = (eval(Money[3:])) / 6.78
    print("USD""%.2f"%(M))
elif Money[0:3] == "USD":
    M = (eval(Money[3:])) * 6.78
    print("RMB""%.2f"%(M))
else:
    print("Error")
