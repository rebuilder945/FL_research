money=input()
if money[0] in ['&']:
    C=(eval(money[1:]))/6.78
    print('%s'%'$'"%.2f"%C)
elif money[0] in ['$']:
    C=(eval(money[1:]))*6.78
    print('%s'%'&'"%.2f"%C)
elif money[:3] in ['RMB']:
    F=(eval(money[2:]))/6.78
    print('%s'%'USD'"%.2f"%F)
elif money[:3] in ['USD']:
    F=(eval(money[2:]))*6.78
    print('%s'%'RMB'"%.2f"%F)
else:
    print("Error")
