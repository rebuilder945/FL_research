a=input()
if a[0]=="$":
    RMB=eval(a[1:-1]+a[-1])*6.78
    print("&{:.2f}".format(RMB))
elif a[0:3] in ["USD","usd"]:
    RMB=eval(a[3:-1]+a[-1])*6.78
    print("RMB{:.2f}".format(RMB))
elif a[0]=="&":
    USD=eval(a[1:-1]+a[-1])/6.78
    print("${:.2f}".format(USD))
elif a[0:3] in ["rmb","RMB"]:
    USD=eval(a[3:-1]+a[-1])/6.78
    print("USD{:.2f}".format(USD))
else:
    print("Error")
