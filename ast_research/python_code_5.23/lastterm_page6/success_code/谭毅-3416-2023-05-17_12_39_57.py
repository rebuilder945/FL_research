a=input()
if a[0] in ['&']:
    M=(eval(a[1:]))/6.78
    print("%.2f$"(M))
elif a[0] in ['RMB']:
    D=(eval(a[1:]))/6.78
    print("%.2fUSD"(D))
elif a[0] in ['$']:
    R=(eval(a[1:]))*6.78
    print("%.2f&"(R))
elif a[0] in ['RMB']:
    B=(eval(a[1:]))*6.78
    print("%.2fUSD"(B))
else:
    print("error")
