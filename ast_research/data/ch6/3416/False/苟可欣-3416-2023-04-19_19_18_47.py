m=input()
if m[0] == "$":
    M=eval(m[1:])*6.78
    print("&%.2f"%(M))
elif m[0] == "&":
    M=eval(m[1:])/6.78
    print("$%.2f"%(M))
elif m[0:3] == "RMB":
    M=eval(m[3:])*6.78
    print("USD%.2f"%(M))
elif m[0:3] == "USD":
    M=eval(m[3:])/6.78
    print("RMB%.2f"%(M))
else:
    print("Error")
