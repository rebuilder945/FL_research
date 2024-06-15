a=eval(input())
if a[0]=="R" :
    b=a/6.78
    print("USD%.2f"%b)
if a[0]=="&":
    b=a/6.78
    print("$%.2f"%b)
if a[0]=="U":
    b=a*6.78
    print("RMB%.2f"%b)
if a[0]=="$":
    b=a*6.78
    print("&%.2f"%b)
