a=list(input())
if a[0]=="$":
    print("&%.2f"%(int(("").join(i for i in a[1::1] ))*6.78))
elif a[0]=="U":
    print("RMB%.2f"%(int(("").join(i for i in a[3::1] ))*6.78))
elif a[0]=="&":
    print("$%.2f"%(int(("").join(i for i in a[1::1] ))/6.78))
elif a[0]=="U":
    print("RMB%.2f"%(int(("").join(i for i in a[3::1] ))/6.78))
else:
    print("Error")


