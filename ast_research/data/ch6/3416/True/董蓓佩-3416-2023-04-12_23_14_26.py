money = input()
def One(money):
    if money[0] == "$":
        sum = eval(money[1:]) * 6.78
        print("&%.2f" % sum)
    elif money[0] == "&":
        sum1 = eval(money[1:]) / 6.78
        print("$%.2f" % sum1)
    else:
        print("Error")


def Three(money):
    if money[:3] == "USD":
        sum2 = eval(money[3:]) * 6.78
        print("RMB%.2f" % sum2)
    elif money[:3] == "RMB":
        sum3 = eval(money[3:]) / 6.78
        print("USD%.2f" % sum3)
    else:
        print("Error")


if money[0] == "$" or money[0] == "&":
    One(money)
elif money[:3] == "RMB" or money[:3] == "USD":
    Three(money)
else:
    print("Error")


