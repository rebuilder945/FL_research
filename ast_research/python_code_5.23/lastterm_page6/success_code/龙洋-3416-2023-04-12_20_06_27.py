x=input()
if x[0]=="$":
    y=float(x[1::])
    qian="&"+"%.2f"%(y*6.78)
elif x[0]=='&':
    y=float(x[1::])
    qian='$'+"%.2f"%(y/6.78)
elif x[0]=='R':
    y=float(x[3::])
    qian="USD"+"%.2f"%(y/6.78)
elif x[0]=='U':
    y=float(x[3::])
    qian='RMB'+"%.2f"%(y*6.78)
print(qian)


