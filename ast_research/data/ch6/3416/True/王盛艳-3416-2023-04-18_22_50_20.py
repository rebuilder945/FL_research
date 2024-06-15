M = input()
if M[0] in ["$"]:
    A = eval(M[1:])*6.78
    print("&%.2f"%(A))
elif M.startswith("USD"):
    RMB = eval(M[3:])*6.78
    print("RMB%.2f"%(RMB))
elif M[0] in ["&"]:
    B = eval(M[1:])/6.78
    print("$%.2f"%(B))
elif M.startswith("RMB"):
    USD = eval(M[3:])/6.78
    print("USD%.2f"%(USD))
else:
    print("Error")

