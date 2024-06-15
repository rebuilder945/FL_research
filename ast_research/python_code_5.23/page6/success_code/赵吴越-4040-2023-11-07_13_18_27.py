q=input()
if q[0]=="$":
    RMB=(eval(q[1:]))*6.78
    print("&""%.2f"%(RMB))
elif q[0:3]=="USD":
    RMB=(eval(q[3:]))*6.78
    print("RMB""%.2f"%(RMB))
elif q[0]=="&":
    USD=(eval(q[1:]))/6.78
    print("$""%.2f"%(USD))
elif q[0:3]=="RMB":
    USD=(eval(q[3:]))/6.78
    print("USD""%.2f"%(USD))
else:
    print("Error")


