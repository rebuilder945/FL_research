a = input()
if a[0] in ["$"]:
    b = (eval(a[1:]))*6.78
    print(f"&{b:.2f}")
elif a[0] in ["&"]:
    b = (eval(a[1:]))/6.78
    print(f"${b:.2f}")
elif a[0] in ["R"]:
    b = (eval(a[3:]))/6.78
    print(f"USD{b:.2f}")
elif a[0] in ["U"]:
    b = (eval(a[3:]))*6.78
    print(f"RMB{b:.2f}")
else:
    print("Error")
