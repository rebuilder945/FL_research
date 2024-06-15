a=list(eval(input()))
a.sort(reverse=True)
for i in a:
 if i!=0:
  print(i,end="")
 else:
    print("0") 
