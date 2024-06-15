MStr= input()
if MStr[0:3] in ['USD']:
    R=(eval(MStr[3:]))*6.78
    print("RMB%.2f"%(R))
elif MStr[0:3] in ['RMB']:
    R=(eval(MStr[3:]))/6.78
    print("USD%.2f"%(R))
elif MStr[0] in ['$']:
    R=(eval(MStr[1:]))*6.78
    print("&%.2f"%(R))
elif MStr[0] in ['&']:
    R=(eval(MStr[1:]))/6.78
    print("$%.2f"%(R))
else:
    print("Error")
    #mon= input()
#if mon[0] in ['$']:
#    C = eval(mon[1:])*6.78 
#    print("&%.2fC"%(C))
#elif mon[0] in ['&']:
#    A = eval(mon[1:])/6.78
#    print("$%.2fA"%(A))
#elif mon[:3] in ['USD']:
#    C = eval(mon[3:])*6.78
#    print("RMB%.2fC"%(C))
#elif mon[:3] in ['RMB']:
#    A = eval(mon[3:])/6.78
#    print("USD%.2f"(A))
#else:
#    print("Error")
#    money = input()
