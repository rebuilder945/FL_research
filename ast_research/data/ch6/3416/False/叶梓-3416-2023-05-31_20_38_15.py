mon= input()

if mon[0] in ['$']:

    C = eval(mon[1:])*6.78 

    print("%.2fC"%(C))

elif mon[0] in ['&']:

    A = eval(mon[1:])/6.78

    print("%.2fA"%(A))

elif mon[0:3] in ['USD']:
    C = eval(mon[3:])*6.78
    print("%.2fC"%(C))
elif mon[0:3] in ['RMB']:
    A = eval(mon[3:])/6.78
else:
    print("Error")
