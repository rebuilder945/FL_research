def switch(x):
    if x[0]=="&":
        a=float(x[1:])/6.78
        return "${:.2f}".format(a)
    elif x[0]=="R":
        a=float(x[3:])/6.78
        return "USD{:.2f}".format(a)
    elif x[0]=="$":
        a=float(x[1:])*6.78
        return "&{:.2f}".format(a)
    elif x[0]=="U":
        a=float(x[3:])*6.78
        return "RMB{:.2f}".format(a)
x=input()
if x[0] not in "&R$U":
    print("Error")
else:
    print(switch(x))
