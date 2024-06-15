a=input()
if a[0] in ['R','&']:
    if a[0] in ['R']:
        b=eval(a[3:])
        c=b/6.78
        print("USD%.2f" %c)
    else:
        b=eval(a[1:])
        c=b/6.78
        print("$%.2f" %c)
elif a[0] in ['U','$']: 
    if a[0] in ['U']:
        b=eval(a[3:])
        c=b*6.78
        print("RMB%.2f" %c)
    else:
        b=eval(a[1:])
        c=b*6.78
        print("&%.2f" %c)
else:
    print("Error")
