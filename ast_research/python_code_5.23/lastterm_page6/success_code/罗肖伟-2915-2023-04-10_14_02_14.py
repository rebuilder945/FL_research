lst=[]
a=eval(input())
if a>=100:
    for i in range(a):
     b=i//100
     c=(i%100)//10
     d=i//10
     if b**3+c**3+d**3==i:
        print(i)
        lst.append(i)
    if len(lst)==0:
     print("none")
else:
  print("none")
   

