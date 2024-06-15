m = input()
if m[0] in ['$', 'U']:
    if m[0] == '$':
        n = float(m[1::])*6.78
        print("&"+"%.2f"%(n))
    else:
        n = float(m[3::])*6.78
        print("RMB"+"%.2f"%(n))
elif m[0] in ['&', "R"]:
    if m[0] == "&":
        n = float(m[1::])/6.78
        print("$"+"%.2f"%(n))
    else:
        n = float(m[3::])/6.78
        print("USD"+"%.2f"%(n))
else:
    print("Error")

