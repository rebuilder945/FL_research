s=input()
if s[0]=="$":
    print("&%.2f"%(int(s[1:])*6.78))
elif s[0]=="&":
    print("$%.2f"%(int(s[1:])/6.78))
elif s[0:3]=="RMB":
    print("USD%.2f"%(int(s[3:])/6.78))
elif s[0:3]=="USD":
    print("RMB%.2f"%(int(s[3:])*6.78))
else:
    print("Error")



