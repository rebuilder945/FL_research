a = input()

if a[0] in ['$']:
    c=(eval(a[1:-1]))*6.78
    print("&%.2f"%(c))
elif a[:3] in ['USD']:
    c=(eval(a[3:]))*6.78
    print("RMB%.2f"%(c))

elif a[0] in ['&']:
    f=(eval(a[1:]))/6.78
    print("$%.2f"%(f))
elif a[:3] in ['RMB']:
    f=(eval(a[3:]))/6.78
    print("USD%.2f"%f)
else:
    print("Error")


