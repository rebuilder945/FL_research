a=input()
b=a[1:]
c=a[3:]
if a.startswith("$"):
    b=eval(b)
    print("&%.2f"%(b*6.78))
elif a.startswith("&"):
    b=eval(b)
    print("$%.2f"%(b/6.78))
elif a.startswith("RMB"):
    c=eval(c)
    print("USD%.2f"%(c/6.78))
elif a.startswith("USD"):
    c=eval(c)
    print("RMB%.2f"%(c*6.78))
else:
    print("Error")


