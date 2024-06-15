a=eval(input())
b=sorted(a,reverse=True)
if b[0:2]in["[0,0]"]:
    print(0)
else:
    for i in range(len(b)):
      print(b[i],end=(""))
    

