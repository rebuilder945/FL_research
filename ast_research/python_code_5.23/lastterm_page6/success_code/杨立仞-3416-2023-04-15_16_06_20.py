qianqianstr=input()
if qianqianstr[0] in ['&']:
    c= (eval(qianqianstr[1:]))/6.78
    print("$%.2f"%(c))
elif qianqianstr[0] in ["R"]:
    b=(eval(qianqianstr[3:]))/6.78
    print("USD%.2f"%(b))
elif qianqianstr[0] in ['$']:
    c= (eval(qianqianstr[1:]))*6.78
    print("&%.2f"%(c))
elif qianqianstr[0] in ['U']:
    c= (eval(qianqianstr[3:]))*6.78
    print("RMB%.2f"%(c))
else:

    print("Error")



