money = input()
if money[0]=="&":
    print("$%.2f"%(eval(money[1:])/6.78))
if money[0]=="$":
    print("&%.2f"%(eval(money[1:])*6.78))
if money[0:3]=="USD":
    print("RMB%.2f"%(eval(money[3:])*6.78))
if money[0:3]=="RMB":
    print("USD%.2f"%(eval(money[3:])/6.78))
else:
    print("Error")
