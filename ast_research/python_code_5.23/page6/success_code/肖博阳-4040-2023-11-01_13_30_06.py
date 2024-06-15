money=input()
list1=["￥"]
list2=["&"]
list3=["USD"]
list4=["RMB"]
       
if money[0] in list1:
    z1=eval(money[1:])*6.78
    print("&%0.2f" % z1)
elif money[0] in list2:
    z2=eval(money[1:])/6.78
    print("$%0.2f" % z2)  

elif money[0:3] in list3:
    z3=eval(money[3:])*6.78
    print("RMB%0.2f" % z3)
elif money[0:3] in list4:
    z4=eval(money[3:])/6.78
    print("USD%0.2f" % z4)  
else:
    print("error")

