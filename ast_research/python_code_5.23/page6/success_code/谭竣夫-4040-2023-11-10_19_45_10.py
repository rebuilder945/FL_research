TempStr = input()
if TempStr[0] in ['R']:
    A = (eval(TempStr[3:999]))/6.78
    print("USD%.2f"%(A))
elif TempStr[0] in ['&']:
    A = (eval(TempStr[1:999]))/6.78
    print("$%.2f"%(A))
elif TempStr[0] in ['U']:
    B = 6.78*eval(TempStr[3:999])
    print("RMB%.2f"%(B))
elif TempStr[0] in ['$']:
    B = 6.78*eval(TempStr[1:999])
    print("&%.2f"%(B))
else:
    print("Error")

