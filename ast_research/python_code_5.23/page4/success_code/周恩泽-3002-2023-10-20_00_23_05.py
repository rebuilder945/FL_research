n1=eval(input())
n2=sum(n1)/len(n1)
if n2%1==0:
  print("%d"%n2)
else:
  print("%.2f"%n2)
