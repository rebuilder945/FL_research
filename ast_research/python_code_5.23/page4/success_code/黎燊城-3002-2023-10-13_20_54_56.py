from tkinter.tix import InputOnly


list=eval(input())
a=sum(list)
b=len(list)
c=a/b
d=a%b
if d==0:
    print("%d"%c)
else:
    print("%.2f"%(c))
