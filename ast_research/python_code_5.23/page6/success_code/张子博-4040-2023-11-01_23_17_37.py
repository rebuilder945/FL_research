x=input()
y=0
if x[0] in "$":
    y=eval(x[1:])*6.78
    print("&"+"%.2f"%y)
elif x[0] in "&":
    y=eval(x[1:])/6.78
    print("$"+"%.2f"%y)
elif x[0:3] in "RMB":
    y=eval(x[1:])/6.78
    print("$"+"%.2f"%y)
elif x[0:3] in "USD":
    y=eval(x[1:])*6.78
    print("&"+"%.2f"%y)
else:
    print("Error")
