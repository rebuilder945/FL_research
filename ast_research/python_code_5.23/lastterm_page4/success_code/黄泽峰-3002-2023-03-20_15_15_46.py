from numpy import average


ls1 = eval(input())
x = average(ls1)
if type(x)== float:
    print("%.2f"%x)
elif type(x)== int:
    print(x)
else:
    print("error")
