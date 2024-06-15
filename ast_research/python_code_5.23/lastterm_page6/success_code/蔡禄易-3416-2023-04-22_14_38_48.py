a = eval(input())
b = eval(input())
if a[0] == ["&"]:
    b = a/6.78
    print("$%.2f"%b)
elif a[0] == ["$"]:
    a = b*6.78
    print("&%.2f"%a)
else:
    print("Error")


