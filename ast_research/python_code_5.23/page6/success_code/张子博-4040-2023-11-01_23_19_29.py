x=input()
y=0
if x[0] in "$":
    y=eval(x[1:])*6.78
    print("&"+"%.2f"%y)
elif x[0] in "&":
    y=eval(x[1:])/6.78
    print("$"+"%.2f"%y)
elif x[0] in "R":
    y=eval(x[3:])/6.78
    print("USD"+"%.2f"%y)
elif x[0] in "U":
    y=eval(x[3:])*6.78
    print("RMB"+"%.2f"%y)
else:
    print("Error")
