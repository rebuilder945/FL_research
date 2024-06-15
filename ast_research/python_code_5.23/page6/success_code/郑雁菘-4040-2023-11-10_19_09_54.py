A = input()
if A[0] == "$":
    B = eval(A[1:])*6.78
    print("&%.2f"%(B))
elif A[0] == '&':
    B = eval(A[1:])/6.78
    print("$%.2f"%(B))
elif A[0] == "U":
    B = eval(A[3:])*6.78
    print("RMB%.2f"%(B))
elif A[0] == "R":
    B = eval(A[3:])/6.78
    print("USD%.2f"%(B))
else:
    print("Error")

