qian=input()
if qian[0]=="$":
    shuzi=qian.lstrip("$")
    shuchu=6.78*float(shuzi)
    c=str("%.2f"%shuchu)
    print("&"+c)
elif qian[0]=="U" and qian[1]=="S":
    shuzi=qian.lstrip("RMBUSD")
    shuchu=6.78*float(shuzi)
    c=str("%.2f"%shuchu)
    print("RMB"+c)
elif qian[0]=="&":
    shuzi=qian.lstrip("&")
    shuchu=float(shuzi)/(6.78)
    c=str("%.2f"%shuchu)
    print("$"+c)
elif qian[0]=="R" and qian[1]=="M":
    shuzi=qian.lstrip("RMB")
    shuchu=float(shuzi)/(6.78)
    c=str("%.2f"%shuchu)
    print("USD"+c)
else:
    print("Error")


