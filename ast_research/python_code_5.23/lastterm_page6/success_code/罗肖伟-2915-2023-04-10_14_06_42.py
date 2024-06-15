lst=[]
a=eval(input())
if 1000>a>=100:
    for i in range(100,a+1):
     b=i//100
     c=(i%100)//10
     d=i%10
     if b**3+c**3+d**3==i:
        print(i)
        lst.append(i)
    if len(lst)==0:
     print("none")
else:
  print("none")
   

