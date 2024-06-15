


a=list(eval(input()))
b=[]
for x in a:
    for i in (2,x):
     if x%i!=0:      
      b.append(x)
      print(b)
    

