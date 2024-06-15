m=input()
if m[0]=="$":
    RMB=eval(m[1:])*6.78
    print("&"+"%.2f"%(RMB))
elif m[0]=="&":
    dollar=eval(m[1:])/6.78
    print("$"+"%.2f"%(dollar))
elif m[:3]=="USD":
    RMB=eval(m[3:])*6.78
    print("RMB"+"%.2f"%(RMB))
elif m[:3]=="RMB":
    USD=eval(m[3:])/6.78
    print("USD"+"%.2f"%(USD))
else:
    print("Error")


