money=input()
def One(money):
    if money[:1]=="$":
        sum=eval(money[1:])*6.78
        print(format(eval(money[1:]),sum))
    elif money[:1]=="&":
        sum=eval(money[1:])/6.78
        print(format(eval(money[1:]),sum))
    else:
        print("Error")
def Three(money):
    if money[:3]=="USD":
        sum=eval(money[3:])*6.78
        print(format(eval(money[3:]),sum))
    elif money[:3]=="RMB":
        sum=eval(money[3:])/6.78
        print(format(eval(money[3:]),sum))
    else:
        print("Error")
if money[:1]=="$" or money[:1]=="&":
    One(money)
elif money[:3]=="USD" or money[:3]=="RMB":
    Three(money)
else:
    print("Error")
