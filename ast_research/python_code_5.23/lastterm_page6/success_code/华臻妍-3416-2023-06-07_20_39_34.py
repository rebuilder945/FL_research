yuan=input()
if yuan[0] in['$']:
    z=(eval(yuan[1:])*6.78)
    print("&""%.2f"%z)
elif yuan[:3] in ["USD"]:
    z=(eval(yuan[3:])*6.78)
    print("RMB""%.2f"%z)
elif yuan[0] in["&"]:
    m=(eval(yuan[1:])/6.78)
    print("$""%.2f"%m)
elif yuan[:3] in ["RMB"]:
    m=(eval(yuan[3:])/6.78)
    print("USD""%.2f"%m)
else:
    print("Error")
