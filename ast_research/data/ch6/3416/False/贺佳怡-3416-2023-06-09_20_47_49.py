x=input()
if x[0]=="&":
    s=(eval(x[1:])/6.78)
    print("$%.2f" % s)
elif x[0]=="$":
    s=(eval(x[1:])*6.78)
    print("&%.2f" % s)
elif x[0]=="R":
    s=(eval(x[3:])/6.78)
    print("USD%.2f" % s)
elif x[0]=="U":
    s=(eval(x[3:])*6.78)
    print("RMB%.2f" % s)
else:
    print("error")




