#月份
a=eval(input())
if 3<=a<=5:
    b=("spring")
elif 6<=a<=8:
    b=("summer")
elif 9<=a<=11:
    b=("autumn")
elif 1<=a<=2 or 12<=a<13:
    b=("winter")
else:
    b=("error")
print(b)

