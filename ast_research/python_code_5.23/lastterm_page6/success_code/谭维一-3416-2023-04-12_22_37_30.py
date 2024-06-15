money = input()
firstchar = money[0]
if firstchar in ["&","$"]:
    if firstchar == "&":
        result = float(money[1:])/6.78
        print(f"${result:.2f}")
    else:
        result = float(money[1:])*6.78
        print(f"&{result:.2f}")
elif firstchar in ["R","U"]:
    if firstchar == "R":
        result = float(money[3:])/6.78
        print(f"USD{result:.2f}")
    else:
        result = float(money[3:])*6.78
        print(f"RMB{result:.2f}")
else:
    print("Error")

