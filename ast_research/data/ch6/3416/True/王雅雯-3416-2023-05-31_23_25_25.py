money = input()
def One(money):
    if money[0]=="$":
        sum = eval(money[1:])*6.78
        return("&{:.2f}".format(sum))
    elif money[0]=="&":
        sum = eval(money[1:])/6.78
        return("${:.2f}".format(sum))
    else:
        print("Error")
def Three(money):
    if money[0:3]=="USD":
        sum = eval(money[3:])*6.78
        return("RMB{:.2f}".format(sum))
    elif money[0:3]=="RMB":
        sum = eval(money[3:])/6.78
        return("USD{:.2f}".format(sum))
    else:
        return("Error")
if money[0] == "$"or money[0] =="&":
    print(One(money))
elif money[0:3] == "RMB"or money[0:3] =="USD":
    print(Three(money))
else:
    print("Error")
