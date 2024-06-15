s=eval(input())
a=sum(s)
b=len(s)
avg=a/b
if type(avg)==int:
   print(int(avg))
if type(avg)==float:
   print("%.2f"%avg)
