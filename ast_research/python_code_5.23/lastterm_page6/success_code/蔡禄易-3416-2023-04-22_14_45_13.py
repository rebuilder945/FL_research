ha = input()
if ha[0] == "$" or ha[0:3] == "USD":
    if ha[0] == "$":
        c = eval(ha[1:])/6.28
        print("&%.2f"%c)
    else:
        c = eval(ha[:3])/6.28
        print("RMB%.2F"%c)
elif ha[0] == "&" or ha[0:3] == "RMB":
    if ha[0] == "&":
        c = eval(ha[1:])*6.28
        print("$%.2f"%c)
    else:
        c = eval(ha[:3])*6.28
        print("USD%.2f"%c)
else:
    print("Error")
