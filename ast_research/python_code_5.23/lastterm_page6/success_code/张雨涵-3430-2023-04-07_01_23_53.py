m = eval(input())
b = ""
if 1<=m<=12:
    if 3<=m<=5:
        b = "spring"
    elif 6<=m<=8:
        b = "summer"
    elif 9<=m<=11:
        b = "autumn"
    else:
        b = "winter"
else:
    b = "error"
print(b)
