qian=input()
if qian[0]is"$":
    yuan=eval(qian[1:])*6.78
    print("&%.2f"%(yuan))
elif qian[0]=="&":
    yuan=eval(qian[1:])/6.78
    print("$%.2f"%(yuan))
elif qian[0:3]=="USD":
    yuan=eval(qian[3:])*6.78
    print("RMB%.2f"%(yuan))
elif qian[0:3]=="RMB":
    yuan=eval(qian[3:])/6.78
    print("USD%.2f"%(yuan))
else:
    print("Error")
