a=input()
if a[0] in ['&']:
    M=(float(a[1:]))/6.78
    print("$%.2f"(M))
elif a[0:3] in ['RMB']:
    D=(float(a[3:]))/6.78
    print("USD%.2f"(D))
elif a[0] in ['$']:
    R=(float(a[1:]))*6.78
    print("&%.2f"(R))
elif a[0:3] in ['USD']:
    B=(float(a[3:]))*6.78
    print("RMB%.2f"(B))
else:
    print("error")
