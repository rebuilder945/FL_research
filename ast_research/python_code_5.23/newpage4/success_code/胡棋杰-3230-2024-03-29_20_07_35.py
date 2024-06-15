a=eval(input())
b=sorted(a,reverse=True)
if b[1:2]in["00"]:
    print(0)
else:
    for i in range(len(b)):
      print(b[i],end=(""))
    

