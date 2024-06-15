money=input()
if money[0] in ['&']:
    C=(eval(money[1:]))/6.78
    print(($)"%.2fC"%)
elif money[0] in ['$']:
    C=(eval(money[1:]))*6.78
    print((&)"%.2fC"%)
elif money[:3] in ['RMB']:
    F=(eval(money[2:]))/6.78
    print((USD)"%.2fF"%)
elif money[:3] in ['USD']:
    F=(eval(money[2:]))*6.78
    print((RMB)"%.2fF"%)
else:
    print("Error")
